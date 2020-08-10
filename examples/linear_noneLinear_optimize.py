import numpy as np
import scipy as sp
import cvxpy as cp
from BasicAction import *


def squre_optimize6_7():
    """二次方优化"""
    x = cp.Variable(5, integer=True)
    x_2 = [1, 1, 3, 4, 2]
    x_1 = [8, 2, 3, 1, 2]

    x_2 = np.array(x_2)
    x_1 = np.array(x_1)
    print(x_1)
    obj = cp.Minimize(x_2 * x ** 2 - x_1 * x)

    conds = [
        cp.sum(x) <= 400,
        cp.sum(cp.multiply(np.array([1, 2, 2, 1, 6]), x)) <= 800,
        cp.sum(cp.multiply(np.array([2, 1, 6, 0, 0]), x)) <= 200,
        cp.sum(cp.multiply(np.array([0, 0, 1, 1, 5]), x)) <= 200,
        x >= 0, x <= 99
    ]
    fun = cp.Problem(obj, conds)
    fun.solve(cp.CPLEX)
    print("the best answer is " + str(fun.value))
    print("the solve is " + str(x.value))


def square_optimize6_6():
    x_2 = [1.5, 1, 0.85]
    x_1 = [3, -8.2, -1.95]
    x = cp.Variable(shape=(3))
    obj = cp.Minimize(x_2 * x ** 2 + x_1 * x)
    cond_matrix = [
        [1, 0, 1],
        [-1, 2, 0],
        [0, 1, 2],
    ]
    value = [2, 2, 3]
    cond_matrix = np.array(cond_matrix)
    cond = [
        cp.sum(cp.multiply(cond_matrix[0], x)) <= value[0],
        cp.sum(cp.multiply(cond_matrix[1], x)) <= value[1],
        cp.sum(cp.multiply(cond_matrix[2], x)) <= value[2],
        cp.sum(x) == 3
    ]
    func = cp.Problem(obj, cond)
    func.solve()
    print(func.value)


def square_optimize_exe6_1():
    cost = [210, 300, 100, 130, 260]
    profit = [150, 210, 60, 80, 180]
    x = cp.Variable(5, integer=True)
    obj = cp.Maximize(cp.sum(cp.multiply(profit, x)))
    conds = [
        cp.sum(cp.multiply(cost, x)) <= 600,
        cp.sum(cp.multiply(np.array([1,1,1,0,0]),x)) == 1,
        cp.sum(cp.multiply(np.array([0,0,1,1,0]),x)) == 1,
        x[0] - x[4] >= 0,
        x >= 0,
        x <= 1,
    ]
    func = cp.Problem(obj, conds)
    func.solve()
    print(func.value)
    print(x.value)


if __name__ == '__main__':
    square_optimize_exe6_1()
