import logging
import os
import datetime

BASE_PATH = '/Volumes/Fast SSD/ModelCom/savedata'


class baseAction():
    """
    basic action
    """

    def __init__(self, basePath=BASE_PATH, log_path='log'):
        """
        init basic action
        :param log_path: the dir of the log
        """
        self.basePath = basePath
        self.logPath = os.path.join(basePath, log_path)
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)
        self.date = datetime.datetime.now()
        self.date = self.date.strftime("%Y%m%d")
        strPath = self.date + '.log'
        logging.basicConfig(
            # 日志级别
            level=logging.INFO,
            # 日志格式
            # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            # 打印日志的时间
            datefmt='%m-%d %Y %H:%M:%S',
            # 日志文件存放的目录（目录必须存在）及日志文件名
            filename=os.path.join(self.logPath, strPath),
            # 打开日志文件的方式
            filemode='a'
        )
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def info(self, msg):
        logging.info(msg)

    def warn(self, msg):
        logging.warning(msg)

    def getDate(self):
        date = datetime.datetime.now()
        strdate = date.strftime("%Y%m%d")
        return strdate

    def getTime(self):
        date = datetime.datetime.now()
        strdate = date.strftime("%H_%M_%S")
        return strdate


if __name__ == '__main__':
    obj = baseAction()
    obj.info("nmsl")
    obj.warn("nimsl")
