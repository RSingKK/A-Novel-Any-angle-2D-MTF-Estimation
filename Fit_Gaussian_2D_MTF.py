import os
import cv2
import math
from osgeo import gdal
from xlwt import *
import numpy as np
import matplotlib.pyplot as plt


### For Example  Samples for Estimating 2D MTF Using Two Dimensional Gaussian function ### x denotes column and y denotes row
x = [0,0,0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.059546516, 0.119093032, 0.178639548, 0.238186063, 0.297732579]
y = [0,0,0, 0.022220583, 0.044441166, 0.06666175, 0.088882333, 0.111102916, 0.060778114, 0.121556229, 0.182334343, 0.243112457, 0.303890572, 0.1, 0.2, 0.3, 0.4, 0.5]
z = [math.log(1), math.log(1), math.log(1), math.log(0.774378342), math.log(0.420633691), math.log(0.190032075), math.log(0.074638962), math.log(0.018506903), math.log(0.697358079), math.log(0.364317657), math.log(0.173864195), math.log(0.036178541), math.log(0.017509105), math.log(0.695323749), math.log(0.426842564), math.log(0.198426071), math.log(0.00419143), math.log(0.000232453)]

x = np.array(x)
y = np.array(y)
z = np.array(z)

a = 1; b = 1; c = 1; d = 1; e = 1
grad_a = 0; grad_b = 0; grad_c = 0; grad_d = 0; grad_e = 0
grad_a_2 = 0; grad_b_2 = 0; grad_c_2 = 0; grad_d_2 = 0; grad_e_2 = 0

time = 1
theta = 0.01

sum_all = []

sum = 10000000
step = 0.01

# while (sum > 6 and pow(math.exp(1), e) <= 1):
while (sum > 11):

    sum = 0
    for i in range(len(x)):

        sum = sum + np.square((a * x[i] * x[i] + b * y[i] * y[i] + c * x[i] + d * y[i] + e - z[i]))
        grad_a = grad_a + 2 * (a * x[i] * x[i] + b * y[i] * y[i] + c * x[i] + d * y[i] + e - z[i]) * x[i] * x[i]
        grad_a_2 = grad_a_2 + 2 * x[i] * x[i] * x[i] * x[i]
        grad_b = grad_b + 2 * (a * x[i] * x[i] + b * y[i] * y[i] + c * x[i] + d * y[i] + e - z[i]) * y[i] * y[i]
        grad_b_2 = grad_b_2 + 2 * y[i] * y[i] * y[i] * y[i]
        grad_c = grad_c + 2 * (a * x[i] * x[i] + b * y[i] * y[i] + c * x[i] + d * y[i] + e - z[i]) * x[i]
        grad_c_2 = grad_c_2 + 2 * x[i] * x[i]
        grad_d = grad_c + 2 * (a * x[i] * x[i] + b * y[i] * y[i] + c * x[i] + d * y[i] + e - z[i]) * y[i]
        grad_d_2 = grad_d_2 + 2 * y[i] * y[i]
        grad_e = grad_e + 2 * (a * x[i] * x[i] + b * y[i] * y[i] + c * x[i] + d * y[i] + e - z[i])
        grad_e_2 = grad_e_2 + 2

    ###Gradient method
    # a = a - step * grad_a; b = b - step * grad_b; c = c - step * grad_c; d = d - step * grad_d; e = e - step * grad_e
    # step = step * 0.92
    ###Newton's method
    a = a - theta * grad_a / grad_a_2; b = b - theta * grad_b / grad_b_2; c = c - theta * grad_c / grad_c_2; d = d - theta * grad_d / grad_d_2; e = e - theta * grad_e / grad_e_2

    time = time + 1
    print(sum)


xx = np.arange(0, 0.5, 0.001)
yy = np.arange(0, 0.5, 0.001)
X, Y = np.meshgrid(xx, yy)

Z = pow(math.exp(1), a * X * X + b * Y * Y + c * X + d * Y + e) / pow(math.exp(1), e)
mtf_A = np.zeros((6,6))
lie = np.array([0,0.1,0.2,0.3,0.4,0.5])
hang = np.array([0,0.1,0.2,0.3,0.4,0.5])

for ii in range (6):
    for jj in range (6):
        mtf_A[ii][jj] = pow(math.exp(1), (a * lie[jj] * lie[jj] + b * hang[ii] * hang[ii] + c * lie[jj] + d * hang[ii] + e)) / pow(math.exp(1), e)
print(mtf_A)


plt.rc('font', family='Times New Roman', size=24, weight='bold')
fig = plt.figure()
ax3 = plt.axes(projection='3d')
ax3.plot_surface(X, Y, Z, cmap='rainbow')
ax3.set_xlabel('Frequency u',labelpad = 16)
ax3.set_ylabel('Frequency v',labelpad = 16)
ax3.set_zlabel('MTF value',labelpad = 16)
plt.show()



