#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 17:15
# @Author  : zc
# @File    : test_C2B_case.py

from Mine.WebSelenium.云平台.子平台.WEB.test_case.page_obj.login_page import Login
from Mine.WebSelenium.云平台.子平台.WEB.test_case.model import mytest,functions
import unittest
from time import sleep

class Test_C2B_Public(mytest.Mytest):

    def verify(self,user='',pwd =''):
        Login(self.driver).login_action(user,pwd)


    def test_login01(self):
        '''用例01：校验弹出框信息'''
        self.verify(user='admin',pwd='123456')
        functions.Functions().screenshot(self.driver,imgName='用例01：校验弹出框信息')
        po = Login(self.driver).error_info()
        self.assertEqual(po,"用户名密码错误",msg='校验信息不一致！')


    def test_login02(self):
        '''用例02：校验菜单信息'''
        self.verify(user='admins',pwd='123456')
        functions.Functions().screenshot(self.driver, imgName='用例02：校验菜单信息')
        po = Login(self.driver).xtgl_text()
        self.assertEqual(po,"系统管理",msg='菜单显示不对！')


if __name__ == '__main__':
    unittest.main()


