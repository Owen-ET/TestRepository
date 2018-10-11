#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/08 17:08
# @Author  : zc
# @File    : untest.py


import unittest
from selenium import webdriver

class UnTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("====class,start!====")


    @classmethod
    def tearDownClass(cls):
        print("====class,stop!====")


    def setUp(self):
        print("=======start!=======")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def tearDown(self):
        print("=======stop!=======")
        pass