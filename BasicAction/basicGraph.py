from BasicAction import *
import os
import matplotlib.pyplot as plt
import numpy as np
import datetime
from mpl_toolkits import mplot3d


class baseGraph(baseAction):
    def __init__(self):
        """
        init 设定存储位置
        """
        super().__init__()
        strdate = self.getDate()
        self.graphDir = os.path.join(self.basePath, 'graphDir' + strdate)
        if not os.path.exists(self.graphDir):
            os.mkdir(self.graphDir)

    def bar(self, listArray, xlables=[], ylable="please input ylable",
            title="please input title", rotation=0, width=0.2, color=None):
        """
        :param listArray:
        :param xlables:
        :param ylable:
        :param title:
        :param rotation: x label旋转角度
        :param width:
        :param color:
        :return:
        """
        data = np.array(listArray)
        self.info("bar :\n titile:" + title + "\n listArray " + str(listArray))
        ind = np.arange(1, data.shape[0] + 1)
        if data.shape[0] != len(xlables):
            self.warn("xlabels:" + str(xlables))
            for _ in range(data.shape[0]):
                xlables.append("x 纬度有误")
        plt.rc('font', size=16)
        plt.bar(ind, data, width, color=color),
        plt.ylabel(ylable)
        plt.xticks(ind, xlables, rotation=rotation)
        # plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.title(title)
        savePath = self.title2Filename(title, 'bar')
        plt.savefig(savePath)
        plt.show()

    def scatter(self, xlist, ylist, title="input title", xlable='input xlable',
                ylable='input ylable', color=['g', 'b', 'yellow', 'lightred']):
        """
        散点图
        :param xlist:
        :param ylist:
        :param title:
        :param xlable:
        :param ylable:
        :param color:
        :return:
        """
        self.info("scatter xlabel" + str(xlable) + "\n ylabel" + str(ylable))
        xdata = np.array(xlist)
        ydata = np.array(ylist)
        if len(xdata.shape) == 1:
            xdata = np.array([xdata])
            ydata = np.array([ydata])
        for i in range(xdata.shape[0]):
            plt.scatter(xdata[i], ydata[i], color=color[i])
        plt.title(title)
        plt.xlabel = ylable
        plt.ylabel = ylable
        savePath = self.title2Filename(title, 'scater')
        plt.savefig(savePath)
        self.info("draw scatter " + str(savePath))
        plt.show()

    def title2Filename(self, title, type):
        """
        图像保存名称 title+type
        :param title:
        :param type:
        :return:
        """
        filename = title.strip(' ').replace(' ', '_')
        now = datetime.datetime.now()
        now = now.strftime("%H_%M_%S")
        filename = filename + now + '_' + type + '.png'
        savePath = os.path.join(self.graphDir, type)
        if not os.path.exists(savePath):
            os.mkdir(savePath)
        savePath = os.path.join(savePath, filename)
        return savePath

    def plot(self, x, y, legend=None, xlable="input xlable", ylable="input ylable", title="input titile",
             color=['r', 'g', 'yellow', 'blue']):
        """
        折线图
        :param x:
        :param y:
        :param legend:
        :param xlable:
        :param ylable:
        :param title:
        :return:
        """

        num = len(x)
        nolegend = False
        if legend is None or len(legend) == 0:
            nolegend = True
            legend = []
            for _ in range(num):
                legend.append("")
        for i in range(num):
            plt.plot(np.array(x[i]), np.array(y[i]), color=color[i], label=legend[i])
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.title(title)
        if not nolegend:
            plt.legend()
        savePath = self.title2Filename(title, 'plot')
        plt.savefig(savePath)
        self.info("draw plot " + str(savePath))
        plt.show()

    def line_3d(self, x, y, z, xtitle="input x", ytitle="input y", ztitle="input z",
                title="input tile"):
        """
        3d 折线图
        :param x:
        :param y:
        :param z:
        :param xtitle:
        :param ytitle:
        :param ztitle:
        :param title:
        :return:
        """
        self.info("line 3d")
        ax = plt.axes(projection='3d')
        ax.plot3D(x, y, z, 'r')
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        ax.set_zlabel(ztitle)
        savePath = self.title2Filename(title, '3d_plot')
        plt.savefig(savePath)
        self.info("draw line3d " + str(savePath))
        plt.show()

    def surface_3d(self, x, y, z, xlable="input x", ylable="input y", zlable="input z",
                   title="input title", cmap='viridis'):
        """
        三维面图
        :param x:
        :param y:
        :param z:
        :param xlable:
        :param ylable:
        :param zlable:
        :param title:
        :return:
        """
        self.info("surface 3d")
        ax = plt.axes(projection='3d')
        plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        ax.set_zlabel(zlable)
        ax.plot_surface(x, y, z, cmap=cmap)
        savePath = self.title2Filename(title, '3d_plot')
        plt.savefig(savePath)
        self.info("draw surface 3d " + str(savePath))
        plt.show()

    def gride_3d(self, x, y, z, xlable="input x", ylable="input y", zlable="input z",
                 title="input title"):
        """
        3d网状图
        :param x:
        :param y:
        :param z:
        :param xlable:
        :param ylable:
        :param zlable:
        :param title:
        :return:
        """
        self.info("grid 3d")
        ax = plt.axes(projection='3d')
        plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        ax.set_zlabel(zlable)
        ax.plot_wireframe(x, y, z, cmap='Accent')
        savePath = self.title2Filename(title, '3d_plot')
        plt.savefig(savePath)
        self.info("draw grid 3d " + str(savePath))
        plt.show()

    def pie(self, percent, lable, colors=None, title="input title",
            autopct="%.1f%%", shadow=True, explode=None):
        """
        饼状图
        """
        self.info("pie graph percentage:" + str(percent))
        plt.pie(percent, labels=lable, colors=colors,
                autopct=autopct, shadow=shadow, explode=explode,
                wedgeprops={'linewidth': 0.5, 'edgecolor': "black"})
        plt.title(title)
        plt.rc('font', size=29)
        savePath = self.title2Filename(title, 'pie')
        plt.savefig(savePath)
        self.info("draw pie " + str(savePath))
        plt.show()

    def contr(self, x, y, z, xlabel="inputx", ylabel="inputY", title="input title"):
        """
        等高线，列优先
        :param x:
        :param y:
        :param z:
        :param xlabel:
        :param ylabel:
        :param title:
        :return:
        """
        contrs = plt.contour(x, y, z)

        plt.clabel(contrs)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        savePath = self.title2Filename(title, 'contr')
        self.info("draw contr " + str(savePath))
        plt.savefig(savePath)
        plt.show()

    def histDrawer(self, x, bin, color='lightblue', orientation='vertical', title='input tile'):
        plt.title(title)
        savePath = self.title2Filename(title, 'hist')
        plt.hist(x, bin, color=color, orientation=orientation)
        plt.savefig(savePath)
        self.info("draw hist " + str(savePath))
        plt.show()

    def sandboxDrawer(self, x, label, title='input_title'):
        plt.title(title)
        savePath = self.title2Filename(title, 'sandbox')
        plt.boxplot(x, labels=label)
        self.info("draw sandbox " + str(savePath))
        plt.savefig(savePath)
        plt.show()


def graphTest():
    matrix = [
        [0., 0., -0.396, -0.9],
        [1., 0., -0.378, -0.882],
        [2., 0., -0.396, -0.882],
        [3., 0., -0.378, -0.9],
        [4., 0., -0.396, -0.882]
    ]
    ret = np.sum(matrix, axis=1)
    xlable = [1, 2, 3, 4, 5]
    print(ret)
    obj = baseGraph()
    obj.bar(ret, xlables=["kehu", "daye", "huangdi", "taijian", "ju"], title="你好", rotation=30, color='r')
    ret2 = []
    for i in ret:
        ret2.append(i - 1)
    obj = baseGraph()
    ylist = [ret, ret2]
    xlist = [xlable, xlable]
    obj.plot(xlist, ylist, legend=["$sin(x)$", "$sin(x^2)$"])
    z = np.linspace(0, 100, 1000)
    x = np.sin(z) * z
    y = np.cos(z) * z
    obj = baseGraph()
    obj.line_3d(x, y, z)
    percent = [1, 2, 3, 4]
    Sum = sum(percent)
    for i in range(len(percent)):
        percent[i] = percent[i] / Sum
    obj = baseGraph()
    obj.pie(percent, ["1", "2", "3", "4"], explode=[0, 0.05, 0, 0])


if __name__ == '__main__':
    obj = baseGraph()
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    obj.scatter(x, y)
