from BasicAction.basicAction import baseAction
from BasicAction import *
from sympy import *
import os
import numpy as np
from scipy.integrate import dblquad


class baseAlgebra(baseAction):
    """
    代数求解
    """

    def __init__(self):
        super().__init__()
        strdate = self.getDate()
        self.algebraDir = os.path.join(self.basePath, 'algebraDir' + strdate)
        if not os.path.exists(self.algebraDir):
            os.mkdir(self.algebraDir)

    def getSymbols(self, Symstr, cls=None):
        """
        返回符号变量
        x,y,z = symbols('x y z')
        """
        if cls is None:
            return symbols(Symstr)
        else:
            return symbols(Symstr, cls=cls)

    def calculateEquation(self, expr, valueDict):
        """

        :param expr:
        :param valueDict:
        :return:
        """
        equation = expr.subs(valueDict)
        ret = expr.subs(valueDict).n()
        self.info("function " + str(equation))
        self.info("function result:" + str(ret))
        return ret

    def limit(self, equation, symbol, limitNum):
        """
        求极限
        :param equation: 公式
        :param symbol: 极限元
        :param limit: 极限
        :return: 极限值 oo代表无穷大
        """
        ret = limit(equation, symbol, limitNum)
        self.info("limit " + str(equation) + " is ====" + str(ret))
        return ret

    def caldiff(self, equation, sym, diffnum):
        """
        求微分
        :param equation: 等式
        :param sym: 参数
        :param diffnum: 微分次方
        :return: 结果方程
        """
        ret = diff(equation, sym, diffnum)
        self.info(str(equation) + " 的关于 " + str(sym) +
                  " 的" + str(diffnum) + " 次方结果为 " + str(ret))
        return ret

    def calIntegrate(self, equation, symANDscope):
        """
        求积分
        :param equation: 公式
        :param symANDscope: 符号和范围（x,0,sympy.pi）
        :return:
        """
        ret = integrate(equation, symANDscope)
        self.info(str(equation) + " 的关于 " + str(symANDscope) +
                  " 的积分结果为 " + str(ret))
        return ret

    def multiIntegrate(self):
        """这仅仅是一个示范"""
        self.info("请自行修改p103")
        fun = lambda x, y: np.exp(-(x ** 2) / 2) * np.sin(x ** 2 + y)
        bd = lambda x: np.sqrt(1 - x ** 2)
        ret = dblquad(fun, -1, 1, lambda x: -bd(x), bd)
        self.info("多重积分求解" + str(ret[0]))

    def matrixResult(self, matrix, value):
        A = Matrix(matrix)
        B = Matrix(value)
        ret = A ** -1
        B = B.transpose()
        ret = ret * B
        self.info("矩阵方程" + str(A) + "=" + str(value) + "的解为：" + str(ret))

    def solve_function(self, equation, symbol):
        """
        方程求解，
        :param equation: 方程，多元方程可以使用【fun1,fun2】
        :param symbol: 求解变量，多元求解可以为【symbol1,symbol2】
        :return: 解值：n重解，默认为1
        """
        try:
            ret = roots(equation, symbol)
        except Exception:
            ret = solve(equation, symbol)
        self.info("fucntion 的解为：" + str(ret))

    def solve_diff_function(self, equation, symbol, ics=None):
        """
        解决微分方程问题
        :param equation:等式
        :param symbol:符号
        :param ics: 边值
        :return:
        """
        ret = dsolve(equation, symbol, ics=ics)
        self.info("funtion result" + str(ret))


if __name__ == '__main__':
    obj = baseAlgebra()
    a = [
        [2, 1, -5, 1],
        [1, -3, 0, -6],
        [0, 2, -1, 2],
        [1, 4, -7, 6]
    ]
    b = [8, 6, -2, 2]
    obj.matrixResult(a, b)
