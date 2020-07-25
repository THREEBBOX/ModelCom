import numpy as np
from BasicAction import *

# dmatrix [xy,d]
d_matrix = np.loadtxt('../data/Pdata17_2.txt')
print(d_matrix.shape)
xy = d_matrix[:, :2]
print("起始坐标经纬度：", xy[0])
d_matrix = d_matrix[:, 2:]
print("距离矩阵大小", d_matrix.shape)

path0 = np.arange(1, 101)
print(path0)
