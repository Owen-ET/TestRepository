#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/28 16:59
# @Author  : zc
# @File    : 新建用户_监察区域人员_page.py

from Autotest.WEB_APP.test_case.page_obj.login_page import SafeLogin
from Autotest.WEB_APP.test_case.models import functions,driver
from selenium.webdriver.common.by import By
from time import sleep


class NewUser(SafeLogin):
    '''新建用户'''

    '''===定位元素==='''
    # 左侧菜单栏：系统管理
    left_xitong_loc = (By.CSS_SELECTOR,"#xitong")
    # iframe
    iframe_loc = (By.TAG_NAME,"iframe")
    # 组织架构
    organizeChart_loc = (By.XPATH,"//div/div[2]/a")
    # 人员管理：工厂区域
    personnel_manageQY_loc = (By.XPATH,"//tbody/tr[3]/td[6]/a[4]")
    # 人员管理：检查小组
    personnel_manageJC_loc = (By.XPATH,"//tbody/tr[5]/td[6]/a[4]")
    # 新增按钮
    add_button_loc = (By.CSS_SELECTOR,".xinzeng")
    # 用户名称
    username_loc = (By.CSS_SELECTOR,"#user_username")
    # 真实姓名
    realname_loc = (By.CSS_SELECTOR,"#user_realname")
    # 手机号
    phoneNum_loc = (By.NAME,"user_phone")
    # 邀请码
    number_loc = (By.CSS_SELECTOR,"input[type=number]")
    # 部门管理者：是
    department_manager_js = "document.getElementsByName('is_not_administrator')[0].click()"
    # 监察人员权限
    inspector_checkbox_js = "document.getElementsByName('renwu[]')[1].click()"
    # 区域人员权限
    regionPeo_checkbox_js = "document.getElementsByName('renwu[]')[2].click()"
    # 用户权限
    user_rights_loc = (By.NAME,"authority_describe")
    # 保存按钮
    save_button_loc = (By.CSS_SELECTOR,".submit")


    '''===操作方法==='''
    def click_left_xitong(self):
        '''点击左侧菜单栏：系统管理'''
        self.click(self.left_xitong_loc)


    def into_iframe(self):
        '''进入iframe'''
        self.enterIfname(self.iframe_loc)


    def click_organizeChart(self):
        '''点击组织架构'''
        self.click(self.organizeChart_loc)


    def click_personnel_manage(self,username):
        '''点击人员管理'''
        self.jc = functions.AllFuncions.jcPerson(self)
        if username == self.jc[0]:
            self.click(self.personnel_manageJC_loc)
        else:
            self.click(self.personnel_manageQY_loc)


    def click_add_button(self):
        '''点击【新增】按钮'''
        self.click(self.add_button_loc)


    def input_username(self,username):
        '''输入用户名称'''
        self.send_keys(self.username_loc,username)


    def input_realname(self,realname):
        '''输入真实姓名'''
        self.send_keys(self.realname_loc,realname)


    def input_phoneNum(self,phoneNum):
        '''输入手机号'''
        self.send_keys(self.phoneNum_loc,phoneNum)


    def input_number(self,num):
        '''输入邀请码'''
        self.send_keys(self.number_loc,num)


    def select_department_Manager(self,username):
        '''选择部门管理者'''
        if username == self.jc[0]:
            self.execute_script(self.department_manager_js)
        else:
            pass


    def select_inspector_checkbox(self,username):
        '''选择权限'''
        if username == self.jc[0]:
            # 监察人员权限
            self.execute_script(self.inspector_checkbox_js)
        else:
            # 区域人员权限
            self.execute_script(self.regionPeo_checkbox_js)


    def select_user_rights(self,text):
        '''选择用户权限'''
        self.select(self.user_rights_loc,text)


    def click_save_button(self):
        '''点击【保存】按钮'''
        self.click(self.save_button_loc)


    def newUser_action(self,username,realname,text):
        '''组织架构操作统一入口'''
        # 登录操作
        SafeLogin(self.driver).login_action()
        self.click_left_xitong()
        self.into_iframe()
        self.click_organizeChart()
        self.click_personnel_manage(username)
        self.click_add_button()
        self.fu = functions.AllFuncions()
        self.input_username(self.fu.getNewName(username)[0])
        self.input_realname(self.fu.getNewName(realname)[0])
        self.input_phoneNum(self.fu.getNewPhoneNum())
        self.input_number(self.fu.getNewName(username)[1])
        self.select_department_Manager(username)
        self.select_inspector_checkbox(username)
        self.select_user_rights(text)
        self.click_save_button()


    '''===断言==='''
    # 姓名
    get_name_loc = (By.XPATH,"//div[@class='bs-example']/form/table/tbody/tr/td[2]")

    def getListName(self,realname):
        '''
        获取列表真实姓名
        :param realname:    真实姓名
        :return:            getRealname
        '''
        # 查询最新输入的姓名
        sleep(0.5)
        getRealname = functions.AllFuncions().getNewName(realname)[2]
        # 定位姓名元素
        names = self.find_elements(*self.get_name_loc)
        lists = []
        for i in names:
            lists.append(i.text)

        # 对比数据库数据与列表数据
        if getRealname in lists:
            return getRealname
        else:
            return None