import sys
import time
import os
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    os.chdir('./report')
    files = os.listdir(os.getcwd())  # 列出目录下的文件
    for file in files:
        if os.path.getsize(file) > 10:
            os.remove(file)  # 删除文件
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='罐车在线接口自动化测试',
                            description='运行环境：MySQL(PyMySQL), Requests, unittest ')

    runner.run(testsuit)
    fp.close()
# import send_email