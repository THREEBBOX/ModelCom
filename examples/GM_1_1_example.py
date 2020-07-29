import numpy as np

data = [25723, 30379, 34473, 38485, 40514, 42400, 48337]  # len=7

add = 0
data_1 = []
for item in data:
    add = add + item
    data_1.append(add)
# 验证是否在GM1—1区间
for i in range(1, len(data)):
    n = i + 1
    print(np.exp(-2 / (n + 1)), np.exp(2 / (n + 1)))
    print(data[i - 1] / data[i])
    print("+++++++++++++++++++")
# z[i] = (x1(k-1)+x(k))/2 k=2......n
zlist = []
for i in range(1, len(data_1)):
    zlist.append((data_1[i] + data_1[i - 1]) / 2)
print(zlist)
print(len(zlist))

zlist = np.array(zlist)
onelist = np.ones_like(zlist)


# 注意负数Z
B = np.c_[-zlist, onelist]
print(B)
Y = np.array(data[1:])
result = np.dot(B.T, B)

result = np.linalg.inv(result)# 求逆矩阵 np.matrix(data) data.I
result = np.dot(result, B.T)
result = np.dot(result, Y)


print(result)
