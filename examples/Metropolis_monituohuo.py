import numpy as np
from BasicAction import *
import matplotlib.pyplot as plt

# dmatrix [xy,d]
d_matrix = np.loadtxt('../data/Pdata17_2.txt')
print(d_matrix.shape)
xy = d_matrix[:, :2]
print("起始坐标经纬度：", xy[0])
d_matrix = d_matrix[:, 2:]
print("距离矩阵大小", d_matrix.shape)

# 寻找较为低代价的起始路径
L = np.inf
for _ in range(2000):
    path0 = np.arange(1, 101)
    np.random.shuffle(path0)

    path0 = np.r_[0, path0, 101]
    L0 = d_matrix[0, path0[1]]
    for i in range(1, 101):
        L0 += d_matrix[path0[i], path0[i + 1]]
    if L0 < L:
        path = path0
        L = L0

print(path)
e = 0.1 ** 30
M = 2000000
at = 0.999  # 退火率
T = 1  # 起始温度

for _ in range(M):
    c = np.random.randint(1, 101, 2)  # 任选两个数字
    c.sort()  # d matrix 只有一半
    c1 = c[0]
    c2 = c[1]
    df = d_matrix[path[c1 - 1], path[c2]] + d_matrix[path[c1], path[c2+1]] \
         - d_matrix[path[c1-1],path[c1]] - d_matrix[path[c2],path[c2+1]]

    if df < 0:
        path = np.r_[path[0], path[1:c1], path[c2:c1-1:-1], path[c2 + 1:102]]
        L += df
    else:
        if np.exp(-df / T) >= np.random.rand(1):
            path = np.r_[path[0], path[1:c1], path[c2:c1 - 1:-1], path[c2 + 1:102]]
            L += df
    T = T * at
    if T < e: break

print(L)
print(path)
xx = xy[path, 0]
yy = xy[path, 1]
obj = baseGraph()
obj.plot([xx], [yy])
