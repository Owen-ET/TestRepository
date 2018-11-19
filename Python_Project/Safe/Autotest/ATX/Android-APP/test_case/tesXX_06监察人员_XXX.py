#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/27 11:13
# @Author  : zc
# @File    : tesXX_06监察人员_XXX.py

import uiautomator2 as u2
import unittest
import uiautomator2.ext.htmlreport as htmlreport
from time import sleep


class TestcitymineSafety(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb('608ad0fe')
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        # hrp = htmlreport.HTMLReport(cls.u, 'report')
        # hrp.patch_click()
        cls.u.toast.show("测试开始", 1.5)

    @classmethod
    def tearDownClass(cls):
        cls.u.toast.show("测试结束", 2)
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
        except:
            print("老版本不获取位置信息！")
        # 输入用户名
        self.d(resourceId="cn.sqm.citymine_safety:id/et_login_id").send_keys("zcjc07")
        self.d.click(0.9, 0.95)
        # 输入密码
        self.d(resourceId="cn.sqm.citymine_safety:id/et_login_password").set_text("111111")
        self.d.click(0.9, 0.95)
        # 点击登录按钮
        self.d(resourceId="cn.sqm.citymine_safety:id/btn_login").click()
        sleep(0.5)

    def tearDown(self):
        print("=======case_stop=======")
        pass

    def testListingThrough(self):  # 复查通过
        # 待复查_复查通过
        # 进入任务栏
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        # 点击待复查
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        # 点击【复查通过】
        listingAgent = "复查通过"
        self.d(text=listingAgent).click()
        # 确定按钮
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_confirm").click()

        # 断言
        # 进入【任务】栏
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_completed").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_the_rectification_progress").click()
        sleep(0.5)
        text = self.d(resourceId="cn.sqm.citymine_safety:id/item_the_rectification_progress_title").get_text()
        print(text)
        self.assertEqual(text,"已整改","复查通过内容显示不对！")

if __name__ == '__main__':
    unittest.main()