from BasicAction.basicAction import *
import pandas as pd
import numpy as np
# todo to_csv index=false 无行号

class baseFile(baseAction):
    """
    基本文件操作类
    """

    def __init__(self):
        """
        设定desecribe 文件存储位置
        """
        super().__init__()
        strdate = self.getDate()
        self.writePath = os.path.join(self.basePath, 'describeDir'+strdate)
        if not os.path.exists(self.writePath):
            os.makedirs(self.writePath)
            self.info("create describe path " + self.writePath)

    def openCSV(self, filename, skiprows=0):
        """
        :param filename:
        :param skiprows:
        :return: np.array data
        """
        matrix = pd.read_csv(filename, skiprows=skiprows,encoding='utf-8')
        self.info("read " + filename + " successful, skip rows:" + str(skiprows))
        describeFrame = matrix.describe()
        describePath = os.path.join(self.writePath, "describe_" +
                                    os.path.split(filename)[1][:-4]+'_' +self.getTime()+ '.xlsx')
        self.info("describe path save in " + describePath)
        fileWriter = pd.ExcelWriter(describePath)
        describeFrame.to_excel(fileWriter, "sheet1")
        fileWriter.save()
        return np.array(matrix)

    def openExcel(self, filename, usecol=None, return_values=True):
        """
        打开文件并describe
        :param filename:
        :param usecol: 使用第几列数据
        :param return_values: ture 返回np.array false返回dataFrame
        :return:
        """
        data = pd.read_excel(filename, usecols=usecol)
        self.info("open " + filename + " success ")
        # save describe
        describeFrame = data.describe()
        describePath = os.path.join(self.writePath, "describe_"
                                    + os.path.split(filename)[1][:-5]+'_'+self.getTime()+'.xlsx')
        self.info("describe path save in " + describePath)

        fileWriter = pd.ExcelWriter(describePath)
        describeFrame.to_excel(fileWriter, "sheet1")
        fileWriter.save()
        if return_values:
            return np.array(data)
        else:
            return data

    def ExcelToCSV(self, filename, usecol=None):
        """
        excel转换CSV
        :param filename:
        :param usecol:
        :return:
        """
        data = pd.read_excel(filename, usecols=usecol)

        path = os.path.splitext(filename)[0] + '.csv'
        self.info("excel to csv " + filename + " to file " + str(path))
        data.to_csv(path)
        self.info(filename + " write to " + path)
    def writeCSV(self,filename):
        #todo
        print(1)
    def writeExc(self,filename):
        print(2)

def filetest():
    obj = baseFile()
    data = obj.openExcel('/Users/wangxy/Documents/ModelCom/data/文件2.xlsx', usecol=[2, 3, 4])
    print(data[:5])
    maxtrix = obj.openCSV('/Users/wangxy/Documents/ModelCom/data/文件1.csv')
    print(maxtrix[0:5])


if __name__ == '__main__':
    filetest()
