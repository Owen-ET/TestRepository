#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/03 11:15
# @Author  : zc
# @File    : test_04区域人员_再次区域整改.py


import uiautomator2 as u2
import unittest
from time import sleep
from Autotest.WEB_APP.test_case.models.functions import AllFuncions


class TestcitymineSafety(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb('608ad0fe')
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        cls.u.toast.show("test_04区域人员_再次区域整改,测试开始", 1.5)


    @classmethod
    def tearDownClass(cls):
        cls.u.toast.show("test_04区域人员_再次区域整改,测试结束", 2)
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

        # 判断密码存不存在
        zcqy = AllFuncions().qyPerson()
        fu = AllFuncions().getNewPwd(zcqy[0])
        username = AllFuncions().getNewName(zcqy[0])[2]
        newPwd = "111111"
        if fu != None:
            '''密码登录'''
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


    def testAgainRegReform(self):  # 再次区域整改
        '''测试用例06：再次区域整改'''
        # 再次整改
        # 进入任务
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        # 点击待整改
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_waiting_for_rectification").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        # 整改：已整改:0、不能整改:1；默认为0，已整改
        text = ["已整改","不能整改"]
        zhengGai = 0
        if zhengGai == 0:
            self.d(text=text[zhengGai]).click()
            self.d(resourceId="cn.sqm.citymine_safety:id/et_has_the_rectification_content").set_text(
                text[zhengGai])
        elif zhengGai == 1:
            self.d(text=text[zhengGai]).click()
            self.d(resourceId="cn.sqm.citymine_safety:id/et_cannot_be_corrected").set_text(text[zhengGai])
        # 选照片
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_select_photos").click()
        self.d(text=u"手机相册").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/v_selected", className="android.widget.ImageView", instance=14).click()
        self.d(resourceId="cn.sqm.citymine_safety:id/done").click()
        # 提交按钮
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_submit").click()
        sleep(0.5)


        # 断言
        # 进入【消息】栏
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_message").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        # 向上滑动
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_violation_management").drag_to(0.2,0,duration=0.5)
        sleep(0.5)
        testText = self.d(resourceId="cn.sqm.citymine_safety:id/tv_the_rectification_content").get_text()
        print(testText)
        print(text[zhengGai])
        self.assertEqual(testText,text[zhengGai],"整改内容显示不对！")