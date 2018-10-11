#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/28 15:15
# @Author  : zc
# @File    : base_page.py

import configparser
from Autotest.WEB_APP.test_case.models import login,driver
from selenium.webdriver.support.select import Select

class Page(object):

    cf = configparser.ConfigParser()
    cf.read(login.configUrl())
    safe_url = cf.get("db", "safeloginurl")

    def __init__(self,webdriver, base_url = safe_url):
        '''
        初始化
        :param webdriver:   定义浏览器
        :param base_url:    基础地址
        '''
        self.driver = webdriver
        self.base_url = base_url
        self.timeout = 10


    def on_page(self):
        '''
        判断系统地址是否正确
        :return:    TRUE/FALSE
        '''
        return self.driver.current_url == self.base_url + self.url


    def open(self):
        '''
        打开系统
        '''
        self._open(self.url)


    def _open(self,url):
        '''
        定义打开系统
        :param url: 小卖安全地址
        '''
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),"url is error:%s" %url


    def find_element(self,*loc):
        '''
        定位单个元素
        :return:    find_element
        '''
        return self.driver.find_element(*loc)


    def find_elements(self,*loc):
        '''
        定位多个元素
        :return:    find_elements
        '''
        return self.driver.find_elements(*loc)


    def send_keys(self,loc,value):
        '''
        输入值操作
        :param loc:     定位元素
        :param value:   值
        '''
        self.find_element(*loc).send_keys(value)


    def click(self,loc):
        '''
        点击操作
        :param loc: 定位元素
        '''
        self.find_element(*loc).click()


    def enterIfname(self,loc):
        '''
        进入iframe操作
        :param loc: 定位元素
        '''
        self.driver.switch_to.frame(self.find_element(*loc))


    def quitIframe(self):
        '''切换回主文档操作'''
        self.driver.switch_to.default_content()


    def execute_script(self,js):
        '''
        js定位元素
        :param js:  js
        '''
        self.driver.execute_script(js)


    def select(self,loc,text):
        '''选择下拉框操作'''
        Select(self.find_element(*loc)).select_by_visible_text(text)


    def getText(self,loc):
        '''获取text值'''
        return self.find_element(*loc).text