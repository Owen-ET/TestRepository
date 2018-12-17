#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 18:06
# @Author  : zc
# @File    : login_page.py

from Mine.WebSelenium.云平台.子平台.WEB.test_case.page_obj.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Login(Page):

    url = ''

    # 用户名
    login_username_loc = (By.CSS_SELECTOR,"#usernamePhone")
    # 密码
    login_password_loc = (By.CSS_SELECTOR,"#pwd")
    # 登录按钮
    login_button_loc = (By.CSS_SELECTOR,".login_button")
    # 登录错误提示信息
    login_error_loc = (By.CSS_SELECTOR,".tips-titles")
    # 移动元素
    move_ele_loc = (By.CSS_SELECTOR,".one_href_img6")
    # js
    js = "document.querySelector('#xtgl > div > span').style.display='block';"
    # 系统管理
    xtgl_loc = (By.CSS_SELECTOR,"#xtgl > div > span")


    def input_user(self,user):
        '''输入用户名'''
        self.input_text(self.login_username_loc,user)


    def input_pwd(self,pwd):
        '''输入密码'''
        self.input_text(self.login_password_loc,pwd)


    def click_button(self):
        '''点击登录'''
        self.click(self.login_button_loc)


    def move_to_element(self):
        '''鼠标悬停'''
        self.move(self.move_ele_loc)


    def xtgl_text(self):
        self.execute_script(self.js)
        return self.get_text(self.xtgl_loc)



    def error_info(self):
        '''登录错误提示'''
        return self.get_text(self.login_error_loc)


    def login_action(self,user,pwd):
        '''
        登录操作统一入口
        :return:
        '''
        self.open()
        self.input_user(user)
        self.input_pwd(pwd)
        self.click_button()
        sleep(0.5)
        # self.xtgl_text()
        # self.driver.quit()


if __name__ == '__main__':
    Login().login_action(user='admins',pwd='123456')