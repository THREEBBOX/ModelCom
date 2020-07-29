import numpy as np
from scipy.optimize import curve_fit

x = [5.081, 4.611, 5.1177, 9.3775, 11.0574, 11.0524]

add = 0
x_1list=[]
for i in x:
    add += i
    x_1list.append(add)

print(x_1list)
t0=np.arange(1,7)
xh2= lambda t,a,b,c: a*np.exp(b*t)+c

para, cov = curve_fit(xh2,t0,x_1list)

print(para)