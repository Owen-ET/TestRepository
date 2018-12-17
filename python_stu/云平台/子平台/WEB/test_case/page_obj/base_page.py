#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 17:26
# @Author  : zc
# @File    : base_page.py

from selenium.webdriver.common.action_chains import ActionChains

class Page(object):

    url = 'http:///login.html#'

    def __init__(self,webdriver,base_url = url):

        self.driver = webdriver
        self.base_url = base_url
        self.timeout = 10


    def on_page(self):
        return self.driver.current_url == self.base_url + self.url


    def open(self):
        self._open(self.url)


    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),"url is error：%s" %url


    def find_element(self,*loc):
        return self.driver.find_element(*loc)


    def click(self,loc):
        self.find_element(*loc).click()


    def input_text(self,loc,text):
        self.find_element(*loc).send_keys(text)


    def execute_script(self,js):
        self.driver.execute_script(js)


    def get_text(self,loc):
        return self.find_element(*loc).text


    def in_frame(self,loc):
        self.driver.switch_to.frame(self.find_element(*loc))


    def out_frame(self):
        self.driver.switch_to.default_content()


    def move(self,loc):
        '''鼠标悬停'''
        move = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(move).perform()