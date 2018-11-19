#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 16:12
# @Author  : zc
# @File    : test.py


# from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import  expected_conditions as EC
# import unittest
# from time import sleep
# from time import sleep
# import Mine.Appium.desired_capabilities as desired_capabilities
#
# # 打开app
# desired_cap = desired_capabilities.get_desired_capabilities()
# uri = desired_capabilities.get_uri()
# driver = webdriver.Remote(uri, desired_cap)
# sleep(10)
# # 输入用户名
# el1 = driver.find_element_by_id("cn.sqm.citymine_safety:id/et_login_id")
# el1.send_keys("zc")

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
# sleep(5)
driver.quit()