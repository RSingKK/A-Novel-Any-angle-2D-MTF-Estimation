from osgeo import gdal
import numpy as np
import cv2
import math
from pylsd.lsd import lsd
from skimage.feature import graycomatrix, graycoprops
from tqdm import tqdm
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import RectangleSelector
from scipy import interpolate
from scipy.signal import savgol_filter
import numpy as np
from skimage import data,filters
from skimage import io
import phasepack
import pyfftw

def deal(data,filename):

    company_name_list = data
    df = pd.DataFrame(company_name_list)
    df.to_excel(filename, index=False)

def sim_DCT(img, height, width):

    img_dct = cv2.dct(img)
    I = np.zeros((im_height, im_width))
    I[0:im_height // 2, 0:im_width // 2] = 1
    I_dct = img_dct * I
    img_denoising = cv2.idct(I_dct)
    return img_denoising

def bilinear_rotate(imgArray, angle, block_H, block_W, translation_y, translation_x):

    H, W = imgArray.shape
    matrix2 = np.array([[math.cos(angle), -math.sin(angle), 0],
                        [math.sin(angle), math.cos(angle), 0],
                        [translation_y, translation_x, 1]])

    new_data = np.zeros([block_H, block_W], dtype=np.uint8)

    for i in range(int(block_H)):
        for j in range(int(block_W)):

            dot2 = np.matmul(np.array([i, j, 1]), matrix2)
            new_coordinate = dot2
            new_i = int(math.floor(new_coordinate[0]))
            new_j = int(math.floor(new_coordinate[1]))
            u = new_coordinate[0] - new_i
            v = new_coordinate[1] - new_j

            if new_j >= W or new_i >= H or new_i < 1 or new_j < 1 or (i + 1) >= H or (j + 1) >= W:
                continue

            if (new_i + 1) >= H or (new_j + 1) >= W:
                new_data[i, j] = imgArray[new_i, new_j]

            else:
                new_data[i, j] = (1 - u) * (1 - v) * imgArray[new_i, new_j] + (1 - u) * v * imgArray[new_i, new_j + 1] + u * (1 - v) * imgArray[new_i + 1, new_j] + u * v * imgArray[new_i + 1, new_j + 1]

    return new_data

file = ['KX10_MII_20230115_E116.53_N40.53_202300007610_L1B']  ### Example Input single satellite scene image
i = 0
j = 0
angle = []
for file_i in range(1):
    print("read filename: " + file[file_i])
    input_scene = 'F:/MTF/' + file[file_i] + '/B1_new.tif'
    dataset = gdal.Open(input_scene)

    im_width = dataset.RasterXSize
    im_height = dataset.RasterYSize
    ccd = dataset.GetRasterBand(1)
    image_data_all = np.array(ccd.ReadAsArray(0, 0, im_width, im_height), dtype=np.uint16)


    for row in tqdm(range(int(im_height / 1000) * 2 - 1)):
        for col in range(int(im_width / 1000) * 2 - 1):
            image_1 = image_data_all[row * 500:(row * 500 + 1000), col * 500:(col * 500 + 1000)]
            dsize = (1000 * 2, 1000 * 2) ### Resampling ×2 or ×3 or ×4
            image_ = cv2.resize(image_1, dsize, 2, 2, interpolation=cv2.INTER_LANCZOS4)  ### Lanczos Interpolation
            width = image_.shape[0]
            height = image_.shape[1]

            image_data = image_.copy()
            image_data_GLCM = image_.copy()

            image_data_255 = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data)) * 255
            image_data_255 = image_data_255.astype(np.uint8)

            image_data_GLCM = (image_data_GLCM - np.min(image_data_GLCM)) / (np.max(image_data_GLCM) - np.min(image_data_GLCM)) * 8
            image_data_GLCM = image_data_GLCM.astype(np.uint8)

            ##
            image_data_denoising = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data)) * 255
            image_data_denoising = image_data_denoising.astype(np.float32)
            image_data_denoising = sim_DCT(image_data_denoising, height, width)
            image_data_denoising = image_data_denoising.astype(np.uint8)
            # image_data_denoising = cv2.GaussianBlur(image_data_255, (3, 3), 1)

            #
            # Line Segment Detection
            linesL = lsd(image_data_denoising)
            ### Thresholds Parameters
            min_line_length = 40
            max_line_length = 70
            gray_difference = 30
            Threshold_IDM = 0.97

            for line in linesL:
                x1, y1, x2, y2 = map(int, line[0:4])
                # print( x1, y1, x2, y2)
                if x1 < x2:
                    x1_new = x1
                    y1_new = y1
                    x2_new = x2
                    y2_new = y2
                if x1 > x2:
                    x1_new = x2
                    y1_new = y2
                    x2_new = x1
                    y2_new = y1
                if x1 == x2:
                    x1_new = x1
                    y1_new = min(y1,y2)
                    x2_new = x1
                    y2_new = max(y1,y2)

                line_length = math.sqrt((x2_new - x1_new) ** 2 + (y2_new - y1_new) ** 2)
                line_length = int(line_length)

                angle_radians = math.asin(abs(y2_new-y1_new)/line_length)
                rotate_radians = math.asin(abs(x2_new-x1_new)/line_length)
                # angle_deg = angle_radians * (180 / math.pi)
                # print(angle_deg)

                if x1_new > 15 and x1_new < width - 15 and x2_new > 15 and x2_new < width - 15 and y1_new > 15 and y1_new < width - 15 and y2_new > 15 and y2_new < width - 15:
                    if line_length >= min_line_length and line_length <= max_line_length:

                        if y1_new <= y2_new:  #Clockwise Rotation, angle < 0

                            left_x_point = x1_new - 15 * np.sin(angle_radians)
                            left_y_point = y1_new + 15 * np.cos(angle_radians)
                            translation_y = int(left_y_point)
                            translation_x = int(left_x_point)

                            rotate_block = bilinear_rotate(image_data_255, -rotate_radians, line_length, 30, translation_y, translation_x)
                            rotate_block_GLCM = bilinear_rotate(image_data_GLCM, -rotate_radians, line_length, 30, translation_y, translation_x)

                        if y1_new > y2_new:  # Counterclockwise Rotation, angle > 0

                            left_x_point = x2_new - 15 * np.sin(angle_radians)
                            left_y_point = y2_new - 15 * np.cos(angle_radians)
                            translation_y = int(left_y_point)
                            translation_x = int(left_x_point)

                            rotate_block = bilinear_rotate(image_data_255, rotate_radians, line_length, 30, translation_y, translation_x)
                            rotate_block_GLCM = bilinear_rotate(image_data_GLCM, rotate_radians, line_length, 30, translation_y, translation_x)

                        left_mean = np.mean(rotate_block[:,0:13])
                        right_mean = np.mean(rotate_block[:,15:29])
                        left_GLCM = graycomatrix(rotate_block_GLCM[:,0:13], [2], [0], 256, symmetric=True, normed=True)
                        left_IDM = graycoprops(left_GLCM, prop='homogeneity')
                        right_GLCM = graycomatrix(rotate_block_GLCM[:,15:29], [2], [0], 256, symmetric=True, normed=True)
                        right_IDM = graycoprops(right_GLCM, prop='homogeneity')

                        # print(rotate_block)
                        # print(line_length)
                        # print(left_mean)
                        # print(right_mean)
                        # print(left_IDM)
                        # print(right_IDM)

                        if abs(left_mean - right_mean) > gray_difference and left_IDM > Threshold_IDM and right_IDM > Threshold_IDM:


                            output_vertical = 'F:/MTF/ROI_B_No_angle/2_new/roi_' + str(i+1) + '.tif'  ### Save Any_angle ROI images
                            driver = gdal.GetDriverByName("GTiff")
                            dataset_vertical = driver.Create(output_vertical, rotate_block.shape[1], rotate_block.shape[0], 1, gdal.GDT_UInt16)
                            dataset_vertical.GetRasterBand(1).WriteArray(rotate_block)
                            dataset_vertical = None

                            angle.append(rotate_radians)

                            i = i + 1
#### Save rotation angle file
deal(angle, 'F:/MTF/ROI_B_No_angle/2_new/2.xlsx')

