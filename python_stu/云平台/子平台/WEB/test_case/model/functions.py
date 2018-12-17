#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 15:44
# @Author  : zc
# @File    : functions.py

import os
from selenium import webdriver

class Functions():

    def screenshot(self,driver,imgName):
        # 获取本文件上一级路径
        base_dir = os.path.dirname(os.path.dirname(__file__))
        # 截取路径并设置截图路径
        img_dir = base_dir.split('test_case')[0] + "report/img/"
        # 截图文件路径
        imgFile = img_dir + imgName + ".png"
        # 截图
        driver.get_screenshot_as_file(imgFile)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    Functions().src(driver,imgName='百度')


