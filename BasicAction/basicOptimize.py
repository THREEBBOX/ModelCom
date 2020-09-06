"""
线性，非线性优化，微分方程求解
"""

from BasicAction import *
import scipy as sp
from scipy import optimize
import os
import cvxpy as cp


class baseOptimize(baseAction):
    def __init__(self):
        super().__init__()
        super().__init__()
        strdate = self.getDate()
        self.optDir = os.path.join(self.basePath, 'optimizeDir' + strdate)
        if not os.path.exists(self.optDir):
            os.mkdir(self.optDir)

    def linear_optimize(self, c, A, b, Aeq, beq, limitTuple):
        """
        对形如：
        min c * X 求最小值（max求反）
        条件为
        A * X <=b
        Aeq * x = beq
        limit((x1.min,x1.max),(x2.min,x2.max))无穷使用None，不分正负无穷
        :param c:
        :param A:
        :param b:
        :param Aeq:
        :param beq:
        :param limitTuple:
        :return:最小值，最佳解
        """
        ret = optimize.linprog(c, A, b, Aeq, beq, limitTuple)
        self.info("最小值为：" + str(ret.fun))
        self.info("最佳解为：" + str(ret.x))
        self.record(c, A, b, Aeq, beq, limitTuple, ret)
        return ret.fun, ret.x

    def record(self, c, A, b, Aeq, beq, limitTuple, ret):
        strdate = self.getDate()
        filepath = 'opt_record_' + strdate + '.txt'
        filepath = os.path.join(self.optDir, filepath)
        f = open(filepath, 'a+')
        f.write(self.getTime() + "\n")
        f.write("minize  " + str(c) + "\n")
        for i in range(len(A)):
            f.write(str(A[i]) + " <= " + str(b[i]) + "\n")
        if Aeq is not None:
            for i in range(len(Aeq)):
                f.write(str(Aeq[i]) + " = " + str(beq[i]) + "\n")
        f.write(str(limitTuple) + "\n")
        f.write("最小值为:" + str(ret.fun) + "\n")
        f.write("最佳解为:" + str(ret.x) + "\n")
        f.write("===============================================================\n")
        f.close()

    def example_multidata(self):
        df1 = pd.read_excel('../data/Pdata5_6.xlsx', header=None)
        data = np.array(df1.values)
        c = data[:-1, :-1]
        d = data[-1, :-1]
        d = d.reshape((1, -1))

        e = data[:-1, -1]
        e = e.reshape((-1, 1))

        x = cp.Variable((6, 8))
        obj = cp.Minimize(cp.sum(cp.multiply(c, x)))
        conds = [
            cp.sum(x, axis=0, keepdims=True) == d,
            cp.sum(x, axis=1, keepdims=True) <= e,
            x >= 0
        ]
        prob = cp.Problem(obj, conds)
        prob.solve(verbose=True)
        print(prob.value)
        print(x.value)

    def example_double_opt(self):

        target = [0.05, 0.27, 0.19, 0.185, 0.185]
        target = np.array(target)
        target = target.reshape(5, 1)
        x = cp.Variable((5, 1))
        obj = cp.Maximize(cp.sum(cp.multiply(target, x)))

        eq = [1, 1.01, 1.02, 1.045, 1.065]
        eq = np.array(eq).reshape(5, 1)
        d = [0.025, 0.015, 0.055, 0.026]
        d = np.array(d).reshape(4, 1)
        value = np.linspace(0, 0.2, 500)
        ret = []
        for a in value:
            alist = [a] * 4
            alist = np.array(alist).reshape(-1, 1)
            conds = [
                cp.sum(cp.multiply(eq, x)) == 1,
                cp.sum(cp.multiply(d, x[1:]), axis=1, keepdims=True) <= alist,
                x >= 0
            ]
            pro = cp.Problem(obj, conds)
            pro.solve()
            ret.append(pro.value)
        return ret


if __name__ == '__main__':
    obj = baseOptimize()
    ret = obj.example_double_opt()
    value = np.linspace(0, 0.2, 500)
    graph = baseGraph()
    graph.scatter([value], [ret])
    # lst=[0,1,2,3,4]
    # print(lst[1:4])
