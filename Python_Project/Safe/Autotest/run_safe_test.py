#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/28 14:36
# @Author  : zc
# @File    : run_safe_test.py


import os
import unittest
import time
from BSTestRunner import BSTestRunner


if __name__ == '__main__':


    # 基础路径
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # 用例路径
    testCase_dir = base_dir + "/WEB_APP/test_case/"
    # 报告路径
    report_dir = base_dir + "/WEB_APP/report/"
    # 报告名字
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    reportName = now + "_report.html"
    reportFile_dir = report_dir + reportName
    # 写入报告文件
    fp = open(reportFile_dir, 'wb')


    # 执行用例
    discover = unittest.defaultTestLoader.discover(testCase_dir,"test*.py")
    # 写入报告
    runner = BSTestRunner(stream=fp,
                          title="小卖安全自动化测试报告：",
                          description="执行下面的用例：")
    # 生成报告
    runner.run(discover)
    fp.close()