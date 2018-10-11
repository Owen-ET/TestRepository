#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/26 17:45
# @Author  : zc
# @File    : test_05监察人员_挂牌待办或复查通过.py

import uiautomator2 as u2
import unittest
from time import sleep
from Autotest.WEB_APP.test_case.models.functions import AllFuncions


class TestcitymineSafety(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb('608ad0fe')
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        cls.u.toast.show("test_05监察人员_挂牌待办或复查通过,测试开始", 1.5)


    @classmethod
    def tearDownClass(cls):
        cls.u.toast.show("test_05监察人员_挂牌待办或复查通过,测试结束", 2)
        cls.u.app_stop_all()
        cls.u.service("uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行


    def setUp(self):
        print("=======case_start=======")
        # 清除数据
        self.u.app_clear("cn.sqm.citymine_safety")
        # 启动小卖安全
        self.d = self.u.session("cn.sqm.citymine_safety")  # restart app
        sleep(0.2)
        # 允许获取位置信息
        try:
            self.d.implicitly_wait(4.5)
            if self.d(resourceId="android:id/alertTitle").exists :
                print("新版本获取位置信息！")
                self.d(resourceId="android:id/button1").click()
            else:
                print("老版本不获取位置信息！")
        except Exception as e:
            print(e)

        zcjc = AllFuncions().jcPerson()
        username = AllFuncions().getNewName(zcjc[0])[2]
        newPwd = "111111"
        # 输入用户名
        self.d(resourceId="cn.sqm.citymine_safety:id/et_login_id").send_keys(username)
        self.d.click(0.9, 0.95)
        # 输入密码
        self.d(resourceId="cn.sqm.citymine_safety:id/et_login_password").set_text(newPwd)
        self.d.click(0.9, 0.95)
        sleep(0.5)
        # 点击登录按钮
        self.d(resourceId="cn.sqm.citymine_safety:id/btn_login").click()
        sleep(0.5)


    def tearDown(self):
        print("=======case_stop=======")
        pass


    def testListingThrough(self):  # 挂牌待办&复查通过
        '''测试用例07：挂牌待办&复查通过'''
        # 待复查_挂牌待办&复查通过
        # 进入任务栏
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        # 点击待复查
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        button = ["挂牌待办","复查通过"]
        # 0：挂牌待办、1：复查通过；默认为1，复查通过
        flag = 1
        if flag == 0:
            # 点击【挂牌待办】按钮
            ListingThrough = button[flag]
            self.d(text=ListingThrough).click()
            # 挂牌待办内容
            sleep(0.5)
            self.d(resourceId="cn.sqm.citymine_safety:id/et_up_to_do_content").set_text(ListingThrough)
            # 确定按钮
            self.d(resourceId="cn.sqm.citymine_safety:id/tv_confirm").click()
            sleep(0.5)

            # 断言
            # 进入【任务】栏
            self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/rb_up_to_do").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
            # 向上滑动
            self.d(resourceId="cn.sqm.citymine_safety:id/tv_violation_management").drag_to(0.2,0,duration=0.5)
            sleep(0.5)
            self.d(resourceId="cn.sqm.citymine_safety:id/rl_rectification_content_and_time").drag_to(0.2,0,duration=0.5)
            sleep(0.5)
            text = self.d(resourceId="cn.sqm.citymine_safety:id/tv_up_to_do_content").get_text()
            print(text)
            self.assertEqual(text,ListingThrough,"挂牌待办内容显示不对！")
        else:
            # 点击【复查通过】按钮
            ListingThrough = button[flag]
            self.d(text=ListingThrough).click()
            # 确定按钮
            self.d(resourceId="cn.sqm.citymine_safety:id/tv_confirm").click()
            sleep(0.5)

            # 断言
            # 进入【任务】栏
            self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/rb_completed").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/rb_the_rectification_progress").click()
            sleep(0.5)
            text = self.d(resourceId="cn.sqm.citymine_safety:id/item_the_rectification_progress_title").get_text()
            print(text)
            self.assertEqual(text, "已整改", "复查通过内容显示不对！")