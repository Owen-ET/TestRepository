#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/26 17:45
# @Author  : zc
# @File    : test_03监察人员_再次发起整改.py

import uiautomator2 as u2
import unittest
from time import sleep
from Autotest.WEB_APP.test_case.models.functions import AllFuncions


class TestcitymineSafety(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb('608ad0fe')
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        cls.u.toast.show("test_03监察人员_再次发起整改,测试开始", 1.5)


    @classmethod
    def tearDownClass(cls):
        cls.u.toast.show("test_03监察人员_再次发起整改,测试结束", 2)
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
        # 点击登录按钮
        self.d(resourceId="cn.sqm.citymine_safety:id/btn_login").click()
        sleep(0.5)


    def tearDown(self):
        print("=======case_stop=======")
        pass


    def testAgainLauReform(self):  # 再次发起整改
        '''测试用例05：再次发起整改'''
        # 待复查_再发起整改
        # 进入任务
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        # 点击待复查
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        # 再次发起整改
        againReform = "发起整改"
        self.d(text=againReform).click()
        # 整改内容
        self.d(resourceId="cn.sqm.citymine_safety:id/et_input_the_rectification_content").set_text("再次" + againReform)
        # 选照片
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_select_photos").click()
        self.d(text=u"手机相册").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/v_selected").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/done").click()
        sleep(0.5)
        # 提交按钮
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_submit").click()
        sleep(0.5)


        # 断言
        # 进入【任务】栏
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        sleep(0.5)
        # 获取再次整改内容
        text = self.d(resourceId="cn.sqm.citymine_safety:id/tv_description_of_hidden_danger").get_text()
        print(text)
        self.assertEqual(text,"再次发起整改","整改内容显示不对！")