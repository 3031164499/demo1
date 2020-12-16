# 导包
import unittest
from script.test01_login import TestLogin
from script.test02_employee import TestEmployee
import app
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

# 组装测试套件
suite = unittest.TestSuite()
suite.addTest(TestLogin("test_login"))
suite.addTest(unittest.makeSuite(TestEmployee))

# 指定报告名称及路径
# report = app.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
report = app.BASE_DIR + "/report/report.html"

# 打开文件流
with open(report, "wb") as f:
    # 创建runner
    runner = HTMLTestRunner(f, title="IHRM接口测试报告")
    # 执行suite
    runner.run(suite)
