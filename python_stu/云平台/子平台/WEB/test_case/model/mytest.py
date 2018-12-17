#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 10:51
# @Author  : zc
# @File    : mytest.py


import unittest
from Mine.WebSelenium.云平台.子平台.WEB.test_case.model.driver import Browser

class Mytest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().browser()
        self.driver.maximize_window()
        print("start!")


    def tearDown(self):
        # self.driver.quit()
        print("stop!")