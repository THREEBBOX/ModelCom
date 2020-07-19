from BasicAction import *
import scipy as sp
import numpy as np
from scipy import stats
from statsmodels.stats import weightstats

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
    def trustField(self,data,alpha):
        """
        置信区间为alpha范围求解
        :param data:
        :param alpha:
        :return:
        """
        df = len(data)-1
        ret = sp.stats.t.interval(alpha,df,loc=data.mean(),scale=sp.stats.sem(data))
        self.info(str(alpha)+"置信区间:"+str(ret))
        return ret
    def calTvalue(self,alpha,n):
        """
        t alpha(n)用于置信区间计算
        请自行除以二
        :param alpha: alpha值，请自行除以二
        :param n: 数量,未减 1 ，请自行减一
        :return:
        """
        ret = sp.stats.t.ppf(1-alpha,n)
        self.info("t "+str(alpha)+"("+str(n)+") = "+str(ret))
        return ret
    def ZtestCal(self,data,value,sigma):
        """
        ztest 计算
        :param data:
        :param value: 标准均值（不是实际均值）
        :param sigma: 标准方差（并非实际方差）
        :return:
        """
        mean = data.mean()

        ret = (mean-value)/(sigma/np.sqrt(data.shape[0]))
        self.info("mean:"+str(mean)+"\nstd:"+str(sigma)+"\n拒绝域："+str(ret))
        return ret






if __name__ == '__main__':
    print("o")
