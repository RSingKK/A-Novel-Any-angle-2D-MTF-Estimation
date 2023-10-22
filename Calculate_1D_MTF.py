from osgeo import gdal
import numpy as np
import cv2
import math
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import RectangleSelector
from scipy import interpolate
from scipy.signal import savgol_filter
import numpy as np
import pandas as pd
from sklearn import linear_model,datasets
from tqdm import tqdm

tao = 10 ** -3
threshold_stop = 10 ** -15
threshold_step = 10 ** -15
threshold_residual = 10 ** -15
residual_memory = []


# construct a user function
def my_Func(params, input_data):
    a = params[0, 0]
    b = params[1, 0]
    c = params[2, 0]
    d = params[3, 0]
    e = math.exp(1)

    ### Logistic Function
    return a / (1 + (pow(e, -(b*(input_data-c))))) + d


# calculating the derive of pointed parameter,whose shape is (num_data,1)
def cal_deriv(params, input_data, param_index):
    params1 = params.copy()
    params2 = params.copy()
    params1[param_index, 0] += 0.000001
    params2[param_index, 0] -= 0.000001
    data_est_output1 = my_Func(params1, input_data)
    data_est_output2 = my_Func(params2, input_data)
    return (data_est_output1 - data_est_output2) / 0.000002


# calculating jacobian matrix,whose shape is (num_data,num_params)
def cal_Jacobian(params, input_data):
    num_params = np.shape(params)[0]
    num_data = np.shape(input_data)[0]
    J = np.zeros((num_data, num_params))
    for i in range(0, num_params):
        a = cal_deriv(params, input_data, i)
        a_ = a.flatten()
        J[:, i] = list(a_)
        # J[:, i] = list(cal_deriv(params, input_data, i))

    return J


# calculating residual, whose shape is (num_data,1)
def cal_residual(params, input_data, output_data):
    data_est_output = my_Func(params, input_data)
    residual = output_data - data_est_output
    return residual


# get the init u, using equation u=tao*max(Aii)
def get_init_u(A, tao):
    m = np.shape(A)[0]
    Aii = []
    for i in range(0, m):
        Aii.append(A[i, i])
    u = tao * max(Aii)
    return u


# LM algorithm
def LM(num_iter, params, input_data, output_data):
    num_params = np.shape(params)[0]  # the number of params
    k = 0
    residual = cal_residual(params, input_data, output_data)
    Jacobian = cal_Jacobian(params, input_data)

    A = Jacobian.T.dot(Jacobian)
    g = Jacobian.T.dot(residual)
    stop = (np.linalg.norm(g, ord=np.inf) <= threshold_stop)  # set the init stop
    u = get_init_u(A, tao)
    v = 2

    while ((not stop) and (k < num_iter)):
        k += 1
        while (1):
            Hessian_LM = A + u * np.eye(num_params)  # calculating Hessian matrix in LM
            step = np.linalg.inv(Hessian_LM).dot(g)  # calculating the update step
            if (np.linalg.norm(step) <= threshold_step):
                stop = True
            else:
                new_params = params + step
                new_residual = cal_residual(new_params, input_data, output_data)
                rou = (np.linalg.norm(residual) ** 2 - np.linalg.norm(new_residual) ** 2) / (step.T.dot(u * step + g))
                if rou > 0:
                    params = new_params
                    residual = new_residual
                    residual_memory.append(np.linalg.norm(residual) ** 2)
                    # print (np.linalg.norm(new_residual)**2)
                    Jacobian = cal_Jacobian(params, input_data)
                    A = Jacobian.T.dot(Jacobian)
                    g = Jacobian.T.dot(residual)
                    stop = (np.linalg.norm(g, ord=np.inf) <= threshold_stop) or (
                                np.linalg.norm(residual) ** 2 <= threshold_residual)
                    u = u * max(1 / 3, 1 - (2 * rou - 1) ** 3)
                    v = 2
                else:
                    u = u * v
                    v = 2 * v
            if (rou > 0 or stop):
                break

    return params

def nan_helper(y):
    # """Helper to handle indices and logical indices of NaNs.
    #
    # Input:
    #     - y, 1d numpy array with possible NaNs
    # Output:
    #     - nans, logical indices of NaNs
    #     - index, a function, with signature indices= index(logical_indices),
    #       to convert logical indices of NaNs to 'equivalent' indices
    # Example:
    #     # >>> # linear interpolation of NaNs
    #     # >>> nans, x= nan_helper(y)
    #     # >>> y[nans]= np.interp(x(nans), x(~nans), y[~nans])
    # """

    return np.isnan(y), lambda z: z.nonzero()[0]

def deal(data,filename):

    company_name_list = data
    df = pd.DataFrame(company_name_list)
    df.to_excel(filename, index=False)

class Compute_MTF(object):

    def __init__(self, filename):

        dataset = gdal.Open(filename)
        im_width = dataset.RasterXSize
        im_height = dataset.RasterYSize
        ccd = dataset.GetRasterBand(1)
        image_data = np.array(ccd.ReadAsArray(0, 0, im_width, im_height), dtype=np.float64)

        image_data = (image_data-np.min(image_data))/(np.max(image_data)-np.min(image_data))*255
        image_data = image_data.astype(np.uint8)
        self.data = image_data.copy()
        self.data_edge = image_data.copy()
        self.min = np.amin(self.data)
        self.max = np.amax(self.data)
#
        self.data_edge = cv2.GaussianBlur(self.data_edge, (3, 3), 1)
        edges = cv2.Canny(self.data_edge, self.min, self.max,apertureSize=3,L2gradient=True)  #L2
        fig = plt.figure()
        plt.subplot(1, 2, 1)
        plt.imshow(edges, cmap='gray')
        plt.title("Detected Edge")

        row_edge, col_edge = np.where(edges == 255)

        z = np.polyfit(np.flipud(col_edge), row_edge, 1)     #calculate the angle of edge

        angle_radians = np.arctan(z[0])
        angle_deg = angle_radians * (180/math.pi)
        print("edge angle:" + str(angle_deg))
        if abs(angle_deg) < 45:
            self.data = np.transpose(self.data)

        im_height_new = self.data.shape[0]
        im_width_new = self.data.shape[1]

        _, th = cv2.threshold(self.data, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        th = th.astype(np.int32)


        self.threshold = np.empty([im_height_new])
        for ii in range(im_height_new):
            below_thresh = ((self.data[ii] >= th[ii]) & (self.data[ii] <= self.max))   #find the 0 value in each line of binery image

            above_thresh = ((self.data[ii] >= self.min) & (self.data[ii] <= th[ii]))   #find the 255 value in each line of binery image

            area_below_thresh = self.data[ii][below_thresh].sum() / below_thresh.sum()
            area_above_thresh = self.data[ii][above_thresh].sum() / above_thresh.sum()

            self.threshold[ii] = (area_below_thresh + area_above_thresh) / 2           #calculate the threshold value of edge column number in each line

        self.compute_esf()
#
    def compute_esf(self):
        kernel = np.ones((3, 3), np.float32)/9
        smooth_img = cv2.filter2D(self.data, -1, kernel)

        row = self.data.shape[0]
        column = self.data.shape[1]

        array_values_near_edge = np.empty([row, 13])
        array_positions = np.empty([row, 13])
        edge_pos = np.empty(row)
        smooth_img = smooth_img.astype(float)
        for i in tqdm(range(0, row)):
            # print(smooth_img[i,:])
            diff_img = smooth_img[i, 1:] - smooth_img[i, 0:(column-1)]
            abs_diff_img = np.absolute(diff_img)
            abs_diff_max = np.amax(abs_diff_img)
            if abs_diff_max == 1:
                raise IOError('No Edge Found')
            app_edge = np.where(abs_diff_img == abs_diff_max)
            bound_edge_left = app_edge[0][0] - 3
            bound_edge_right = app_edge[0][0] + 4

            strip_cropped = self.data[i, bound_edge_left:bound_edge_right]    #8 pixels


            strip_cropped = np.unique(strip_cropped)

            temp_y = np.arange(1, strip_cropped.size+1)


            strip_cropped = strip_cropped.reshape((len(strip_cropped),1))
            temp_y = temp_y.reshape((len(temp_y),1))
            params = np.ones((4, 1))
            num_iter = 100  # the number of iteration
            est_params_left = LM(num_iter, params, strip_cropped, temp_y)
            # print(est_params)
            a_est_left = est_params_left[0, 0]
            b_est_left = est_params_left[1, 0]
            c_est_left = est_params_left[2, 0]
            d_est_left = est_params_left[3, 0]
            e = math.exp(1)

            ###Logistic Function
            edge_pos_temp =  a_est_left / (1 + (pow(e, -(b_est_left * (self.threshold[i] - c_est_left))))) + d_est_left
            edge_pos[i] = edge_pos_temp + bound_edge_left - 1
            bound_edge_left_expand = app_edge[0][0] - 6
            bound_edge_right_expand = app_edge[0][0] + 7
            array_values_near_edge[i, :] = self.data[i, bound_edge_left_expand:bound_edge_right_expand]
            array_positions[i, :] = np.arange(bound_edge_left_expand, bound_edge_right_expand)

        y = np.arange(0, row)
        nans, x = nan_helper(edge_pos)
        edge_pos[nans] = np.interp(x(nans), x(~nans), edge_pos[~nans])

        array_positions_by_edge = array_positions - np.transpose(edge_pos * np.ones((13, 1)))   #以边缘列为（0,0）

        num_row = array_positions_by_edge.shape[0]
        num_col = array_positions_by_edge.shape[1]

        array_values_by_edge = np.reshape(array_values_near_edge, num_row*num_col, order='F')
        array_positions_by_edge = np.reshape(array_positions_by_edge, num_row*num_col, order='F')

        bin_pad = 0.0001
        pixel_subdiv = 0.10
        topedge = np.amax(array_positions_by_edge) + bin_pad + pixel_subdiv
        botedge = np.amin(array_positions_by_edge) - bin_pad

        binedges = np.arange(botedge, topedge+1, pixel_subdiv)
        numbins = np.shape(binedges)[0] - 1

        binpositions = binedges[0:numbins] + (0.5) * pixel_subdiv
        whichbin = np.digitize(array_positions_by_edge, binedges)
        binmean = np.empty(numbins)

        for i in range(0, numbins):
            flagbinmembers = (whichbin == i)

            binmembers = array_values_by_edge[flagbinmembers]
            binmean[i] = np.mean(binmembers)
        nans, x = nan_helper(binmean)
        binmean[nans] = np.interp(x(nans), x(~nans), binmean[~nans])
        esf = binmean
        xesf = binpositions
        xesf = xesf - np.amin(xesf)
        self.xesf = xesf
        esf_smooth = savgol_filter(esf, 51, 3)
        self.esf = esf
        self.esf_smooth = esf_smooth
        self.compute_lsf()
#

    def compute_lsf(self):
        diff_esf = abs(self.esf[1:] - self.esf[0:(self.esf.shape[0] - 1)])
        diff_esf = np.append(0, diff_esf)
        lsf = diff_esf
        diff_esf_smooth = abs(self.esf_smooth[0:(self.esf.shape[0] - 1)] - self.esf_smooth[1:])
        diff_esf_smooth = np.append(0, diff_esf_smooth)
        lsf_smooth = diff_esf_smooth
        self.lsf = lsf
        self.lsf_smooth = lsf_smooth
        self.compute_mtf()

#
    def compute_mtf(self):
        mtf = np.absolute(np.fft.fft(self.lsf, 2048))
        mtf_smooth = np.absolute(np.fft.fft(self.lsf_smooth, 2048))
        mtf_final = np.fft.fftshift(mtf)
        mtf_final_smooth = np.fft.fftshift(mtf_smooth)
        plt.subplot(1, 2, 2)
        x_mtf_final = np.arange(0,1,1./127)
        mtf_final = mtf_final[1024:1151]/np.amax(mtf_final[1024:1151])
        mtf_final_smooth = mtf_final_smooth[1024:1151]/np.amax(mtf_final_smooth[1024:1151])
        plt.plot(x_mtf_final, mtf_final_smooth, linewidth=1.5, color='black')
        plt.xlabel("cycles/pixel")
        plt.ylabel("Modulation Factor")
        blue_patch = mpatches.Patch(color='black', label='MTF')
        plt.legend(handles=[blue_patch])
        plt.show()
        return mtf_final_smooth
#
if __name__ == '__main__':

    mtff = Compute_MTF("./ROI.tif") ###Input Any_angle ROI file, extracted from Step One
    mtf = mtff.compute_mtf()
    deal(mtf, './MTF.xlsx')   ### Save the calculated 1D MTF values




