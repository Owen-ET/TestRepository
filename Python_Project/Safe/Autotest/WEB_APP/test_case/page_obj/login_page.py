#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/28 16:12
# @Author  : zc
# @File    : login_page.py

import Autotest.WEB_APP.test_case.models.login as login
from time import sleep
from Autotest.WEB_APP.test_case.page_obj.base_page import Page


class SafeLogin(Page):

    url = ''

    def userLogin(self):
        '''用户登录'''
        # 获取cookie登录
        value = login.safeLogin()
        self.driver.add_cookie({"name": "PHPSESSID", "value": value})
        # 页面刷新
        sleep(0.5)
        self.driver.refresh()
        sleep(0.5)


    def login_action(self):
        '''登录操作统一入口'''
        self.open()
        self.userLogin()