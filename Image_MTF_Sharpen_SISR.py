import cv2 as cv
import cv2
import numpy as np
from numpy import *
import math
from scipy import signal
from scipy import fftpack
import cv2
from osgeo import gdal
from matplotlib import pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']

def FFT_denoising(FF_array):
    FF_array = np.float64(FF_array)
    im_height = FF_array.shape[0]
    im_width = FF_array.shape[1]
    FF = fftpack.fftn(FF_array)
    F_magnitude = np.abs(FF)
    F_magnitude = fftpack.fftshift(F_magnitude)
    K = 30
    F_magnitude[im_height // 2 - K: im_height // 2 + K, im_width // 2 - K: im_width // 2 + K] = 0
    peaks = F_magnitude < np.percentile(F_magnitude, 98)  # for 98 percentile
    peaks = fftpack.ifftshift(peaks)
    F_dim = FF.copy()  # for 98 percentile
    F_dim = F_dim * peaks.astype(int)  # for 98 percentile
    image_filtered = np.real(fftpack.ifft2(F_dim))  # for 98 percentile

    return image_filtered


def matrixExtend(mtx,k):
    r_m = np.ones((k,mtx.shape[0]))
    c_m = np.ones((k,mtx.shape[0]+k))
    mtx = np.row_stack((mtx, r_m))
    mtx = np.column_stack((mtx, c_m.T))

    return mtx

### Array Symmetry
def array_symmetry(a):
    a = np.array(a)
    d = np.copy(a)

    for k in range(len(a[0])):
        d[:, k] = a[:, len(a[0]) - 1 - k]

    dd = np.hstack((d[:, 0:(len(a[0]) - 1)], a))

    ddd = np.copy(dd)

    for kk in range(len(dd)):
        ddd[kk, :] = dd[len(dd) - 1 - kk, :]

    dddd = np.vstack((ddd[0:(len(dd) - 1), :], dd))
    return dddd

### Array Extend
def array_extension(a):
    b_i = []
    bb_i = []
    data_i = []
    b_j = []
    bb_j = []
    data_j = []
    a = np.array(a)
    last = len(a) - 1

    for i in range(len(a)):
        for ii in range(last):
            data_i = (linspace(a[i][ii], a[i][ii + 1], 61))
            b_i = np.hstack((b_i, data_i[0:60]))
        b_i = np.hstack((b_i, a[i][last]))
        bb_i.append(b_i)
        b_i = []
    aa = np.array(bb_i)

    for j in range(len(aa[0])):
        for jj in range(last):
            data_j = (linspace(aa[jj][j], aa[jj + 1][j], 61))
            b_j = np.hstack((b_j, data_j[0:60]))
        b_j = np.hstack((b_j, aa[last][j]))
        bb_j.append(b_j)
        b_j = []

    aaa = np.transpose(np.array(bb_j))

    return aaa

### MTF Filter
def restore_image(aa):
    extension = array_extension(aa)

    D_lie1 = np.copy(extension[0, :])
    DD_lie1 = np.copy(extension[0, :])

    len_D_lie_w = len(np.where(D_lie1 > 0.5)[0])
    for i in range(D_lie1.shape[0]):
        if i < (len_D_lie_w - 1):
            DD_lie1[i] = 1
        else:
            DD_lie1[i] = 0.5 * (1 + math.cos(math.pi * ((i - (len_D_lie_w - 1))) / ((D_lie1.shape[0] - 1) - (len_D_lie_w - 1))))
    D_hang1 = np.copy(extension[:, 0])
    DD_hang1 = np.copy(extension[:, 0])
    len_D_hang_w = len(np.where(D_hang1 > 0.5)[0])
    print(len_D_hang_w - 1)
    for i in range(D_hang1.shape[0]):
        if i < (len_D_hang_w - 1):
            DD_hang1[i] = 1
        else:
            DD_hang1[i] = 0.5 * (1 + math.cos(math.pi * ((i - (len_D_hang_w - 1))) / ((D_hang1.shape[0] - 1) - (len_D_hang_w - 1))))

    p_M = np.transpose(np.outer(DD_hang1, DD_lie1))
    p_M_ = array_symmetry(p_M)

    return p_M_

##### Example, Input 2D MTF from Step Three
mtf_RGB = [[[1, 0.68650264, 0.38740262, 0.17970536, 0.0685232, 0.02147793],
            [0.73159331, 0.50224074, 0.28342117, 0.13147124, 0.05013112, 0.01571311],
            [0.55290033, 0.37956754, 0.21419504, 0.09935915, 0.0378865, 0.01187515],
            [0.43164962, 0.29632861, 0.1672222, 0.07756975, 0.02957801, 0.00927094],
            [0.34811543, 0.23898216, 0.13486083, 0.06255821, 0.02385398, 0.0074768],
            [0.29001642, 0.19909704, 0.11235312, 0.05211751, 0.01987285, 0.00622895]],
           [[1, 0.78485268, 0.54785939, 0.34012839, 0.18780601, 0.0922293],
            [0.7495571,0.5882919, 0.41065189, 0.25494565, 0.14077133, 0.06913113],
            [0.49240577, 0.38646599, 0.26976912, 0.16748118, 0.09247676, 0.04541424],
            [0.28350142, 0.22250685, 0.15531891, 0.09642688, 0.05324327, 0.02614714],
            [0.14305434, 0.11227658, 0.07837366, 0.04865684, 0.02686646, 0.0131938],
            [0.06326456, 0.04965336, 0.03466008, 0.02151807, 0.01188147, 0.00583485]],
           [[1, 0.76257862, 0.51337502, 0.30510569, 0.16007789, 0.07414432],
            [0.61718924, 0.47065532, 0.31684954, 0.18830795, 0.09879835, 0.04576108],
            [0.33235768, 0.25344886, 0.17062413, 0.10140422, 0.05320312, 0.02464243],
            [0.15615724, 0.11908217, 0.08016723, 0.04764446, 0.02499732, 0.01157817],
            [0.06401586, 0.04881712, 0.03286414, 0.0195316, 0.01024752, 0.00474641],
            [0.02289718, 0.0174609, 0.01175484, 0.00698606, 0.00366533, 0.0016977]]]

#### Input Single Satellite Scene Image for SSIR
dataset_1 = gdal.Open('./a.tif')

width = dataset_1.RasterXSize
height = dataset_1.RasterYSize
im_bands = dataset_1.RasterCount
im_width = width * 2  ###×2 ×3 ×4
im_height = height * 2 ###×2 ×3 ×4
driver = gdal.GetDriverByName("GTiff")
dataset = driver.Create('./a_', im_width, im_height, 3, gdal.GDT_UInt16)
dsize = (im_width,im_height)
for band in range(3):  #RGB Image

    extension = array_extension(mtf_RGB[band])
    symmetry = array_symmetry(extension)
    symmetry = np.array(symmetry)
    p_w = (1 / symmetry) * ((symmetry * symmetry) / (symmetry * symmetry + 0.04))
    im_data_1 = dataset_1.GetRasterBand(band+1)
    print(band)
    im_dataa_1 = np.array(im_data_1.ReadAsArray(0, 0, width, height), dtype=np.float64)
    im_dataa_1 = cv2.resize(im_dataa_1, dsize, 2, 2, interpolation=cv2.INTER_LANCZOS4) ### resampling ×2 ×3 ×4
    im_dataa_1_extend = matrixExtend(im_dataa_1,1)
    f = np.fft.fft2(im_dataa_1_extend)
    fshift = np.fft.fftshift(f)
    res = 20 * np.log(np.abs(fshift))
    fshift_juan = fshift * p_w  # WF Filter
    ishift = np.fft.ifftshift(fshift_juan)
    iimg = np.fft.ifft2(ishift)
    iimg_ = np.abs(iimg)
    # iimg_[iimg_ > 4096] = 4096
    iimg_[iimg_ > 255] = 255
    iimg_x2 = iimg_[0:im_width,0:im_height]
    ### Save SISR results
    dataset.GetRasterBand(band+1).WriteArray(iimg_x2)


