#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/08 16:54
# @Author  : zc
# @File    : test_00新建用户_监察人员和区域人员.py

import unittest
from Autotest.WEB_APP.test_case.page_obj.新建用户_监察区域人员_page import NewUser
from Autotest.WEB_APP.test_case.models import functions,untest
from time import sleep


class TestCase(untest.UnTest):


    # 初始化：执行新建用户操作
    def verify(self,username='',realname='',text=''):
        NewUser(self.driver).newUser_action(username,realname,text)


    @unittest.skipIf(1 < 0,"正确直接跳过！")
    def test_newInspectorUser(self):
        '''测试用例01：新建监察人员'''
        # 监察人员参数
        fu = functions.AllFuncions()
        jc = fu.jcPerson()
        text = "超级管理员"
        # 截图序号
        num = str(fu.getNewName(jc[0])[1])
        self.verify(jc[0],jc[1],text)
        po = NewUser(self.driver).getListName(jc[1])
        sleep(2)
        print(po)
        functions.AllFuncions().screenshot(self.driver, imgName=num + "新建监察人员_" + po)
        self.assertEqual(po,"zc监察1","查询最新监察人员与列表中不符！")


    @unittest.skipUnless(1 > 0,"错误就强制跳过！")
    def test_newRegionPeoUser(self):
        '''测试用例02：新建区域人员'''
        # 区域人员参数
        fu = functions.AllFuncions()
        qy = fu.qyPerson()
        text = "审批管理员"
        # 截图序号
        num = str(fu.getNewName(qy[0])[1])
        self.verify(qy[0],qy[1],text)
        po = NewUser(self.driver).getListName(qy[1])
        sleep(2)
        print(po)
        functions.AllFuncions().screenshot(self.driver, imgName=num + "新建区域人员_" + po)
        self.assertEqual(po,"zc区域1","查询最新区域人员与列表中不符！")