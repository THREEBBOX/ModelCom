from BasicAction import *
import scipy as sp
import numpy as np
from scipy import stats
from statsmodels.stats import weightstats
from scipy import interpolate


# pdf概率密度
# cdf概率
class basePro(baseAction):
    def __init__(self):
        super().__init__()

    def normPro(self, mean, std, num):
        """
        正态分布在 x<num 的概率
        :param mean:
        :param std:
        :param num:
        :return:
        """
        ret = stats.norm.cdf(num, mean, std)
        self.info("正态分布 mean" + str(mean) + " std "
                  + str(std) + "|||小于" + str(num) + "的概率分布为" + str(ret))
        return ret

    def normProBetween(self, mean, std, numB, numE):
        """
        范围内的概率
        :param mean:
        :param std:
        :param numB: begin
        :param numE: end
        :return:
        """
        ret1 = self.normPro(mean, std, numE)
        ret2 = self.normPro(mean, std, numB)
        ret = ret1 - ret2
        self.info("正态分布 mean" + str(mean) + " std "
                  + str(std) + "范围" + str(numB) + "～"
                  + str(numE) + "的概率分布为" + str(ret))
        return ret

    def drawNorm(self, mean, std, times=2):
        x = np.linspace(mean - times * std, mean + times * std, 100)
        y = stats.norm.pdf(x)
        obj = baseGraph()
        obj.plot([x], [y])

    def drawHist(self, x, bin, color='lightblue', orientation='vertical', title='input tile'):
        obj = baseGraph()
        obj.histDrawer(x, bin, color=color, orientation=orientation, title=title)

    def drawSandbox(self, x, label, title='input title'):
        obj = baseGraph()
        obj.sandboxDrawer(x, label, title=title)

    def trustField(self, data, alpha):
        """
        置信区间为alpha范围求解
        :param data:
        :param alpha:
        :return:
        """
        df = len(data) - 1
        ret = sp.stats.t.interval(alpha, df, loc=data.mean(), scale=sp.stats.sem(data))
        self.info(str(alpha) + "置信区间:" + str(ret))
        return ret

    def calTvalue(self, alpha, n):
        """
        t alpha(n)用于置信区间计算
        请自行除以二
        :param alpha: alpha值，请自行除以二
        :param n: 数量,未减 1 ，请自行减一
        :return:
        """
        ret = sp.stats.t.ppf(1 - alpha, n)
        self.info("t " + str(alpha) + "(" + str(n) + ") = " + str(ret))
        return ret

    def ZtestCal(self, data, value, sigma):
        """
        ztest 计算 用来处理拒绝域
        :param data:
        :param value: 标准均值（不是实际均值）
        :param sigma: 标准方差（并非实际方差）
        :return:
        """
        mean = data.mean()

        ret = (mean - value) / (sigma / np.sqrt(data.shape[0]))
        self.info("mean:" + str(mean) + "\nstd:" + str(sigma) + "\n拒绝域：" + str(ret))
        return ret

    # 一维插值法'
    def dataInsertion_linear(self, data, range, title="data insertion result"):
        """
        数据量较少，或者数据量之间空间比较大，这时候需要插如更多的值来进行计算，补足空缺
        线性插值法
        :param data: 原始[x,y]
        :param range: 插值范围
        :return:
        """
        func = interpolate.interp1d(data[0], data[1])
        ret = func(range)
        self.info(str(data) + "\n插值结果为：\n" + str(ret))
        graph = baseGraph()
        graph.scatter([range], [ret], title=title)
        return ret

    def dataInsertion_cubic(self, data, range, title="data insertion result"):
        """
        三次样条插值法
        :param data:
        :param range:
        :param title:
        :return:
        """
        func = interpolate.interp1d(data[0], data[1], 'cubic')
        ret = func(range)
        self.info(str(data) + "\n插值结果为：\n" + str(ret))
        graph = baseGraph()
        graph.scatter([range], [ret], title=title)
        return ret

    def dataInsertion_2D(self, data, x, y, rangx, rangy, titile="data insertion 3d"):
        """
        先列后行，二维插值法
        :param data:
        :param x:行范围
        :param y:列范围
        :param rangx:行插值范围
        :param rangy:列插值范围
        :param titile:
        :return:
        """
        f = interpolate.interp2d(y, x, data, 'cubic')
        zn = f(rangy, rangx)
        return zn

    def fit_example(self):
        """
        fit 函数选择，P228
        可二维你和
        :return:
        """
        x = np.linspace(0, 1, 11)
        y = np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])
        f = np.polyfit(x, y, 2)
        import matplotlib.pyplot as plt
        plt.scatter(x, y, c='r')
        yhat = np.polyval(f, x)
        plt.plot(x, yhat, color='lightblue')
        plt.show()
        print(f)

    def fit_example_3d(self):
        x = np.array([6, 2, 6, 7, 4, 2, 5, 9])
        y = np.array([4, 9, 5, 3, 8, 5, 8, 2])
        z = np.array([5, 2, 1, 9, 7, 4, 3, 3])
        xy0=np.vstack((x,y))
        print(xy0.shape)
        def pfunc(t,a,b,c):
            return a*np.exp(b*t[0])+c*t[1]**2
        from scipy.optimize import curve_fit
        popt,pcov = curve_fit(pfunc,xy0,z)
        print(popt)
        return popt



if __name__ == '__main__':
    data = np.loadtxt('/Volumes/Fast SSD/ModelCom/data/Pdata7_5.txt')
    print(data.shape)
    data = data[::-1]
    print(data.shape)
    x = np.arange(0, 1300, 100)
    print(x.shape)
    y = np.arange(0, 1500, 100)
    print(y.shape)
    f = interpolate.interp2d(y, x, data)
    xn = np.linspace(0, 1200, 121)
    yn = np.linspace(0, 1400, 141)
    zn = f(yn, xn)

    graph = baseGraph()
    print("=====")
    print(zn.shape)
    print(xn.shape)
    print(yn.shape)
    graph.contr(yn, xn, zn)
