from osgeo import gdal
import os
from xlwt import *
import pandas as pd
import numpy as np
import cv2
import math
import random
from PIL import Image
from skimage.metrics import structural_similarity
from skimage.metrics import peak_signal_noise_ratio
from tqdm import tqdm

def deal(data,filename):

    company_name_list = data

    df = pd.DataFrame(company_name_list)

    df.to_excel(filename, index=False)
from image_similarity_measures.evaluate import evaluation
ff_HR = ["F:/MTF/HR_x2/"]
ff_solved = ["F:/MTF/SSIR_results/"]
file_output = ['F:/MTF/assessment.xlsx']

for file_LR in range(1):
    roots_HR = str(ff_HR[0])
    roots_solved = str(ff_solved[file_LR])
    a = []
    for root, _, files in os.walk(roots_HR):
        for file in tqdm(files):

            absfile_HR = os.path.join(root, file)
            absfile_solved = os.path.join(roots_solved, file)

            dataset_1 = gdal.Open(absfile_HR)
            dataset_2 = gdal.Open(absfile_solved)

            HR_img_shape = dataset_1.RasterXSize
            solved_img_shape = dataset_2.RasterXSize

            HR_img = np.zeros((HR_img_shape, HR_img_shape, 3))
            solved_img = np.zeros((solved_img_shape, solved_img_shape, 3))
            for i in range(3):
                HR_img_ = dataset_1.GetRasterBand(i+1)
                HR_img[:,:,i] = np.array(HR_img_.ReadAsArray(0, 0, HR_img_shape, HR_img_shape), dtype=np.float16)
                HRR = HR_img[:, :, i].copy()
                solved_img_ = dataset_2.GetRasterBand(i+1)
                solved_img_normalize = np.array(solved_img_.ReadAsArray(0, 0, solved_img_shape, solved_img_shape), dtype=np.float16)

                solved_img[:, :, i] = (solved_img_normalize-np.min(solved_img_normalize))/(np.max(solved_img_normalize)-np.min(solved_img_normalize))*(np.max(HRR)-np.min(HRR)) + np.min(HRR)


            if solved_img.shape[0] != HR_img.shape[0]:
                img_stack_sm = np.zeros((HR_img.shape[0], HR_img.shape[0], 3))
                for idx in range(3):
                    img = solved_img[:, :, idx]
                    img_sm = cv2.resize(img, (HR_img.shape[0], HR_img.shape[0]), interpolation=cv2.INTER_LANCZOS4)
                    img_stack_sm[:, :, idx] = img_sm

                img_stack_sm_singleband = img_stack_sm[:,:,0]
                sum = 0
                for band in range(3):
                    for i in range(HR_img.shape[0] - 1):
                        for j in range(HR_img.shape[0] - 1):
                            sum = sum + np.sqrt((img_stack_sm[i + 1][j][band] - img_stack_sm[i][j][band]) ** 2 + (img_stack_sm[i][j + 1][band] - img_stack_sm[i][j][band]) ** 2 / 2)

                GMG = sum / (HR_img.shape[0] * HR_img.shape[0] * 3)
                laplacian=cv2.Laplacian(img_stack_sm,cv2.CV_64F)
                LS = np.sum(abs(laplacian)) / (HR_img.shape[0] * HR_img.shape[0] * 3)
                HR_img = HR_img.astype(np.byte)
                img_stack_sm = img_stack_sm.astype(np.byte)
                SSIM = structural_similarity(HR_img, img_stack_sm, data_range=255, multichannel=True, win_size=5, channel_axis=2)
                PSNR = peak_signal_noise_ratio(HR_img, img_stack_sm)

            else:
                sum = 0
                for band in range(3):
                    for i in range(HR_img.shape[0] - 1):
                        for j in range(HR_img.shape[0] - 1):
                            sum = sum + np.sqrt((solved_img[i + 1][j][band] - solved_img[i][j][band]) ** 2 + (solved_img[i][j + 1][band] - solved_img[i][j][band]) ** 2 / 2)
                GMG = sum / (HR_img.shape[0] * HR_img.shape[0] * 3)
                laplacian=cv2.Laplacian(solved_img,cv2.CV_64F)
                LS = np.sum(abs(laplacian)) / (HR_img.shape[0] * HR_img.shape[0] * 3)

                HR_img = HR_img.astype(np.byte)
                solved_img = solved_img.astype(np.byte)
                SSIM = structural_similarity(HR_img, solved_img, data_range=255, multichannel=True, win_size=5, channel_axis=2)
                PSNR = peak_signal_noise_ratio(HR_img, solved_img)
            B = [file,SSIM,PSNR,GMG,LS]
            a.append(B)
    deal(a,file_output[file_LR])


print(SSIM)
print(PSNR)
print(GMG)
print(LS)



