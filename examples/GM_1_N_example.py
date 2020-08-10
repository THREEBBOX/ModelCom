import numpy as np

data = np.loadtxt('../data/Pdata15_3.txt')

x10 = data[:, 0]
x20 = data[:, 1]
x30 = data[:, 2]
x40 = data[:, 3]

x11 = np.cumsum(x10)
x21 = np.cumsum(x20)
x31 = np.cumsum(x30)
x41 = np.cumsum(x40)

z1 = (x11[:-1] + x11[1:]) / 2
z2 = (x21[:-1] + x21[1:]) / 2
z3 = (x31[:-1] + x31[1:]) / 2
z4 = (x41[:-1] + x41[1:]) / 2

B = np.c_[-z1, z2, z3, z4]

Y = np.array(data)
Y = data[1:, ]
n = 13
B1 = np.c_[z1, np.ones((n - 1, 1))]
u1 = np.linalg.pinv(B1).dot(x10[1:]);
print(u1)
B2 = np.c_[z1, z2]
u2 = np.linalg.pinv(B2).dot(x20[1:]);
print(u2)
B3 = np.c_[z3, np.ones((n - 1, 1))];
u3 = np.linalg.pinv(B3).dot(x30[1:]);
print(u3)
B4 = np.c_[z1, z3, z4]
u4 = np.linalg.pinv(B4).dot(x40[1:]);
print(u4)


# 设置方程
def Pfun(x, t):
    x1, x2, x3, x4 = x
    return np.array(
        u1[0] * x1 + u1[1],
        u2[0] * x1 + u2[1] * x2,
        u3[0] * x3 + u3[1],
        u4[0] * x1 + u4[1] * x3 + u4[2] * x4
    )
