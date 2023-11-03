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
from sklearn.linear_model import RANSACRegressor

def oneD_RANSAC(array_ransac):
    data = array_ransac

    # RANSAC Parameters
    num_iterations = 100
    sample_size = 2
    # threshold = 0.4
    threshold = 0.3


    best_model = None
    best_inliers = []
    best_num_inliers = 0

    for _ in range(num_iterations):
        # Randomly Select two samples
        random_indices = np.random.choice(len(data), size=sample_size, replace=False)
        sampled_data = data[random_indices]
        model = np.polyfit(random_indices, sampled_data, 1)
        # Calculate Error
        errors = np.abs(data - np.polyval(model, np.arange(len(data))))
        # Calculate iliers and outliers
        inliers = np.where(errors < threshold)[0]
        outliers = np.where(errors > threshold)[0]
        num_inliers = len(inliers)
        # Updata Model
        if num_inliers > best_num_inliers:
            best_num_inliers = num_inliers
            best_inliers = inliers
            outlines = outliers
            best_model = model
    return outlines

###  Levenberg-Marquardt Parameters

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
    k = 0  # set the init iter count is 0
    # calculating the init residual
    residual = cal_residual(params, input_data, output_data)
    # calculating the init Jocobian matrix
    Jacobian = cal_Jacobian(params, input_data)

    A = Jacobian.T.dot(Jacobian)  # calculating the init A
    g = Jacobian.T.dot(residual)  # calculating the init gradient g
    stop = (np.linalg.norm(g, ord=np.inf) <= threshold_stop)  # set the init stop
    u = get_init_u(A, tao)  # set the init u
    v = 2  # set the init v=2

    while ((not stop) and (k < num_iter)):
        k += 1
        while (1):
            Hessian_LM = A + u * np.eye(num_params)  # calculating Hessian matrix in LM
            step = np.linalg.inv(Hessian_LM).dot(g)  # calculating the update step
            if (np.linalg.norm(step) <= threshold_step):
                stop = True
            else:
                new_params = params + step  # update params using step
                new_residual = cal_residual(new_params, input_data, output_data)  # get new residual using new params
                rou = (np.linalg.norm(residual) ** 2 - np.linalg.norm(new_residual) ** 2) / (step.T.dot(u * step + g))
                if rou > 0:
                    params = new_params
                    residual = new_residual
                    residual_memory.append(np.linalg.norm(residual) ** 2)
                    # print (np.linalg.norm(new_residual)**2)
                    Jacobian = cal_Jacobian(params, input_data)  # recalculating Jacobian matrix with new params
                    A = Jacobian.T.dot(Jacobian)  # recalculating A
                    g = Jacobian.T.dot(residual)  # recalculating gradient g
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
        if row_edge.size == 0 or col_edge.size == 0:
            print("No Edge Found!")
        else:
            z = np.polyfit(np.flipud(col_edge), row_edge, 1)     # Calculate incidence angle of edge

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
                below_thresh = ((self.data[ii] >= th[ii]) & (self.data[ii] <= self.max))   # Find 0 position in binary image

                above_thresh = ((self.data[ii] >= self.min) & (self.data[ii] <= th[ii]))   # Find 255 position in binary image

                area_below_thresh = self.data[ii][below_thresh].sum() / below_thresh.sum()
                area_above_thresh = self.data[ii][above_thresh].sum() / above_thresh.sum()

                self.threshold[ii] = (area_below_thresh + area_above_thresh) / 2           #Calculate the gray value threshold of edge in each row

            self.compute_esf()
            


#
    def compute_esf(self):

        kernel = np.ones((3, 3), np.float32)/9
        smooth_img = cv2.filter2D(self.data, -1, kernel)
        row = self.data.shape[0]
        column = self.data.shape[1]
        array_values_near_edge = np.zeros([row, 13])
        array_positions = np.zeros([row, 13])
        edge_pos = np.zeros(row)
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

            strip_cropped = self.data[i, bound_edge_left:bound_edge_right]    # 8 pixels
            strip_cropped = np.unique(strip_cropped)
            if self.threshold[i] < np.max(strip_cropped) and self.threshold[i] > np.min(strip_cropped) and (app_edge[0][0] - 6) > 0 and (app_edge[0][0] + 7) < column:
                temp_y = np.arange(1, strip_cropped.size + 1)
                # f = interpolate.interp1d(strip_cropped, temp_y, kind='cubic')
                # edge_pos_temp = f(self.threshold[i])

                strip_cropped = strip_cropped.reshape((len(strip_cropped), 1))  ### LM
                temp_y = temp_y.reshape((len(temp_y), 1))
                params = np.ones((4, 1))
                num_iter = 100  # the number of iteration
                est_params_left = LM(num_iter, params, strip_cropped, temp_y)
                a_est_left = est_params_left[0, 0]
                b_est_left = est_params_left[1, 0]
                c_est_left = est_params_left[2, 0]
                d_est_left = est_params_left[3, 0]

                e = math.exp(1)

                ## Logistic function
                edge_pos_temp = a_est_left / (1 + (pow(e, -(b_est_left * (self.threshold[i] - c_est_left))))) + d_est_left

                edge_pos[i] = edge_pos_temp + bound_edge_left - 1
                bound_edge_left_expand = app_edge[0][0] - 6
                bound_edge_right_expand = app_edge[0][0] + 7
                array_values_near_edge[i, :] = self.data[i, bound_edge_left_expand:bound_edge_right_expand]
                array_positions[i, :] = np.arange(bound_edge_left_expand, bound_edge_right_expand)
            else:
                print("The threshold value calculated by Otsu+Binary is abnormal,and the" + str(i) + "-th row is deleted")
        non_empty_ = edge_pos != 0
        edge_pos_ = edge_pos[non_empty_]
        non_empty_rows1 = np.any(array_values_near_edge != 0, axis=1)
        array_values_near_edge_ = array_values_near_edge[non_empty_rows1]
        non_empty_rows2 = np.any(array_positions != 0, axis=1)
        array_positions_ = array_positions[non_empty_rows2]

        #### RANSAC remove outliers from the detected edge positions

        indices_to_remove = oneD_RANSAC(edge_pos_)
        edge_pos_ransac = edge_pos_[np.logical_not(np.isin(np.arange(len(edge_pos_)), indices_to_remove))]
        array_values_near_edge_ransac = array_values_near_edge_[~np.isin(np.arange(array_values_near_edge_.shape[0]), indices_to_remove)]
        array_positions_ransac = array_positions_[~np.isin(np.arange(array_positions_.shape[0]), indices_to_remove)]

        y = np.arange(0, row)
        nans, x = nan_helper(edge_pos_ransac)
        edge_pos_ransac[nans] = np.interp(x(nans), x(~nans), edge_pos_ransac[~nans])
#
        array_positions_by_edge = array_positions_ransac - np.transpose(edge_pos_ransac * np.ones((13, 1)))
        num_row = array_positions_by_edge.shape[0]
        num_col = array_positions_by_edge.shape[1]

        array_values_by_edge = np.reshape(array_values_near_edge_ransac, num_row*num_col, order='F')
        array_positions_by_edge = np.reshape(array_positions_by_edge, num_row*num_col, order='F')
#
        bin_pad = 0.0001
        pixel_subdiv = 0.10
        topedge = np.amax(array_positions_by_edge) + bin_pad + pixel_subdiv
        botedge = np.amin(array_positions_by_edge) - bin_pad

        binedges = np.arange(botedge, topedge+1, pixel_subdiv)
        numbins = np.shape(binedges)[0] - 1

        binpositions = binedges[0:numbins] + (0.5) * pixel_subdiv

        whichbin = np.digitize(array_positions_by_edge, binedges)
        binmean = np.empty(numbins)
#
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
        MTF_withfrequency = list(zip(x_mtf_final, mtf_final_smooth))
        plt.plot(x_mtf_final, mtf_final_smooth, linewidth=1.5, color='black')
        plt.xlabel("cycles/pixel")
        plt.ylabel("Modulation Factor")
        blue_patch = mpatches.Patch(color='black', label='MTF')
        plt.legend(handles=[blue_patch])
        plt.show()
        return MTF_withfrequency

if __name__ == '__main__':

    mtff = Compute_MTF("F:/MTF/ROI_A_No_angle/roi_5.tif")
    mtf = mtff.compute_mtf()
    deal(mtf, 'F:/MTF/ROI_A_No_angle/shiyan_roi_5.xlsx')



