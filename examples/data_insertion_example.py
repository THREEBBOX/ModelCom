from BasicAction import *


def example_linear_data_insertion():
    """
    一维度，线性插值法
    """
    x = np.arange(0, 25, 2)
    y = [12, 9, 9, 10, 18, 24, 28, 27, 25, 20, 18, 15, 13]
    y = np.array(y)
    newrange = np.linspace(0, 24, 200)
    obj = basePro()
    obj.dataInsertion_linear([x, y], range=newrange)


def example_cubic_data_insertion():
    """
    一维度，三次样条插值法
    """
    x = np.arange(0, 25, 2)
    y = [12, 9, 9, 10, 18, 24, 28, 27, 25, 20, 18, 15, 13]
    y = np.array(y)
    newrange = np.linspace(0, 24, 200)
    obj = basePro()
    obj.dataInsertion_cubic([x, y], range=newrange)


def example_2D_data_insertion():
    """
    二维插值
    :return:
    """
    data = np.loadtxt('/Volumes/Fast SSD/ModelCom/data/Pdata7_5.txt')
    print(data.shape)
    data = data[::-1]
    print(data.shape)
    x = np.arange(0, 1300, 100)
    print(x.shape)
    y = np.arange(0, 1500, 100)
    print(y.shape)
    obj = basePro()
    xn = np.linspace(0, 1200, 121)
    yn = np.linspace(0, 1400, 141)
    zn = obj.dataInsertion_2D(x, y, xn, yn)

    graph = baseGraph()
    print("=====")
    print(zn.shape)
    print(xn.shape)
    print(yn.shape)
    graph.contr(yn, xn, zn)


def fit_examples():
    obj = basePro()
    obj.fit_example()


def pfunc(t, a, b, c):
    return a * np.exp(b * t[0]) + c * t[1] ** 2


def fit_3D_examples():
    obj = basePro()
    ret = obj.fit_example_3d()
    x = np.linspace(2, 9, 701)
    y = np.linspace(2, 9, 701)
    z = np.ones(shape=(701, 701))
    for i in range(701):
        for k in range(701):
            z[i][k] = pfunc([x[i], y[k]], *ret)
    graph = baseGraph()
    graph.surface_3d(x, y, z)


if __name__ == '__main__':
    fit_3D_examples()
