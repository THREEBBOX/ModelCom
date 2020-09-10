import numpy as np


data = [9.6,18.3,29,47.2,71.1,119.1,174.6,
        257.3,350.7,441.0,513.3,559.7,594.8,
        629.4,640.8,651.1,655.7,659.6,661.8]
data = np.array(data)
time=np.arange(0,19)

matrix1 = np.c_[data[:-1],-data[:-1]**2]
matrix2 = np.array(data[1:]-data[:-1])
print(matrix2)
#%%
result = np.linalg.pinv(matrix1).dot(matrix2)
print(result)
x0 = data[0]
xn=0;
rlist = [x0]
r = result[0]
N = result[0] / result[1]
print(N)
for i in range(1,19):
    xn = x0+r*x0*(1-x0/N)
    x0 = xn
    rlist.append(xn)
print(rlist)
#%%
import matplotlib.pyplot as plt
import pylab as mpl
plt.figure()
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
plt.scatter(time,data,color='r',marker='*')
plt.plot(time,rlist,color='b')
plt.title("拉屎")
plt.xlabel("拉屎")
plt.legend(("s","d"))

plt.show()