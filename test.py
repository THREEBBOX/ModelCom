from BasicAction import *
import numpy as np


def shuangqumina():
    """
    双曲面
    :return:
    """
    theta = np.linspace(-np.pi, np.pi, 40)
    fi = np.linspace(-np.pi, np.pi, 40)
    THETA, FI = np.meshgrid(theta, fi)
    z = np.power(6, 0.5) * np.tan(THETA)
    y = np.power(10, 0.5) * (1 / np.cos(THETA)) * np.cos(FI)
    x = np.power(8, 0.5) * (1 / np.cos(THETA)) * np.sin(FI)
    obj = baseGraph()
    obj.surface_3d(x, y, z, cmap=None)


def denggaoxina():
    """
    等高线
    :return:
    """
    obj = baseGraph()
    x = np.linspace(-2, 2, 50)
    y = np.linspace(-2, 3, 50)
    x, y = np.meshgrid(x, y)
    z = x * np.exp(-x * x - y * y)
    obj.contr(x, y, z)


def fangxiangweifen():
    """方向微分"""
    v = 1
    d = 200
    time = 400
    T = np.linspace(0, 400, 400)
    xy = [
        [-d, d],
        [d, d],
        [d, -d],
        [-d, -d]
    ]
    xy = np.array(xy)
    dt = T[1] - T[0]
    Txy = xy
    xyn = np.empty((4, 2))
    for n in range(len(T)):
        for i in range(4):
            j = (1 + i) % 4
            dxy = xy[j] - xy[i]
            dd = dxy / np.linalg.norm(dxy)
            xyn[i] = xy[i] + v * dd * dt
        Txy = np.c_[Txy, xyn]
        xy = xyn.copy()
    xlist = []
    ylist = []
    for i in range(4):
        xlist.append(Txy[i, ::2])
        ylist.append(Txy[i, 1::2])
    obj = baseGraph()
    obj.plot(xlist, ylist, legend=['a', 'b', 'c', 'd'])


if __name__ == '__main__':
    a =np.array([429,358,434,445,527])
    print(a.mean())

