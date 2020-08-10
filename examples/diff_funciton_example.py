"""
微分方程求解
"""
from BasicAction import *
from sympy.abc import x
from sympy import diff, dsolve, simplify, Function, sin
import sympy as sp


def symbol_sovle():
    """
    符号解法
    p236 8-1
    """
    y = Function('y')
    eq = diff(y(x), x, 2) + 2 * diff(y(x), x) + 2 * y(x)
    con = {
        y(0): 0,
        diff(y(x), x).subs(x, 0): 1
    }
    y = dsolve(eq, ics=con)
    print(simplify(y))


def symbol_solve_2():
    """
    8.2
    :return:
    """
    y = Function('y')
    eq = diff(y(x), x, 2) + 2 * diff(y(x), x) + 2 * y(x) - sin(x)
    con = {
        y(0): 0,
        diff(y(x), x).subs(x, 0): 1
    }
    y = dsolve(eq, ics=con)
    print(simplify(y))


def symbol_solve_3():
    """
    8.3
    :return:
    """
    x1, x2, x3 = sp.symbols('x1,x2,x3', cls=sp.Function)
    t = sp.symbols('t')

    eq = [
        2 * x1(t) - 3 * x2(t) + 3 * x3(t) - diff(x1(t), t),
        4 * x1(t) - 5 * x2(t) + 3 * x3(t) - diff(x2(t), t),
        4 * x1(t) - 4 * x2(t) + 2 * x3(t) - diff(x3(t), t)
    ]
    con = {
        x1(0): 1,
        x2(0): 2,
        x3(0): 3
    }
    s = sp.dsolve(eq, ics=con)
    print(simplify(s[0]))
    print(simplify(s[1]))
    print(simplify(s[2]))
def double_diff():
    """
    8.7
    :return:
    """
    t,k=sp.symbols('t,k')
    u = sp.Function('u')
    eq = sp.diff(u(t),t)+k*(u(t)-24)
    """一个等式一个值"""
    con ={
        u(0):150
    }
    uu = sp.dsolve(eq,ics=con)
    print("uu",uu)
    kk= sp.solve(uu,k)
    print("kk",kk)
    k0=kk[0].subs(
        {
            t:10,
            u(t):100
        }
    )
    print(k0)
    u1=uu.args[1]
    print("u1",u1)
    u0=u1.subs({
        t:20,
        k:k0
    })
    print(4400/63)

if __name__ == '__main__':
    double_diff()
