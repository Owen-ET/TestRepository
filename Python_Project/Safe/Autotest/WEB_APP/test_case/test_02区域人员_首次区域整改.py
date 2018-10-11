#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/03 11:15
# @Author  : zc
# @File    : test_02区域人员_首次区域整改.py


import uiautomator2 as u2
import unittest
from time import sleep
from Autotest.WEB_APP.test_case.models.functions import AllFuncions


class TestcitymineSafety(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb('608ad0fe')
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        cls.u.toast.show("test_02区域人员_首次区域整改,测试开始", 1.5)


    @classmethod
    def tearDownClass(cls):
        cls.u.toast.show("test_02区域人员_首次区域整改,测试结束", 2)
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
            # 点击登录按钮
            self.d(resourceId="cn.sqm.citymine_safety:id/btn_login").click()
            sleep(0.5)
        else:
            '''邀请码登录'''
            print("邀请码登录")
            self.d(resourceId="cn.sqm.citymine_safety:id/rb_verification_code_login").click()
            self.yqm = AllFuncions().getNewName(zcqy[0])[3]
            # 输入用户名
            self.d(resourceId="cn.sqm.citymine_safety:id/et_login_id").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/et_login_id").set_text(username)
            self.d.click(0.9, 0.95)
            # 输入邀请码
            self.d(resourceId="cn.sqm.citymine_safety:id/et_login_password").set_text(self.yqm)
            self.d.click(0.9, 0.95)
            # 点击登录按钮
            self.d(resourceId="cn.sqm.citymine_safety:id/btn_login").click()
            '''设置登录密码'''
            # 新密码
            self.d(resourceId="cn.sqm.citymine_safety:id/et_new_password").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/et_new_password").set_text(newPwd)
            # 确认新密码
            self.d(resourceId="cn.sqm.citymine_safety:id/et_reconfirm_new_password").click()
            self.d(resourceId="cn.sqm.citymine_safety:id/et_reconfirm_new_password").set_text(newPwd)
            sleep(0.5)
            # 点击保存按钮
            self.d(resourceId="cn.sqm.citymine_safety:id/tv_save").click()
            sleep(1)


    def tearDown(self):
        print("=======case_stop=======")
        pass


    def testRegReform(self):  # 区域整改
        '''测试用例04：首次区域整改'''
        # 新用户登录：修改个人信息
        try:
            if self.d(text=u"修改个人信息").exists:
                print("新用户登录修改个人信息！")
                # 头像
                self.d(resourceId="cn.sqm.citymine_safety:id/img_header").click()
                self.d(text=u"手机相册").click()
                sleep(0.5)
                self.d.click(0.5, 0.15)
                sleep(0.5)
                self.d.click(0.6, 0.6)
                # 职务
                self.d(resourceId="cn.sqm.citymine_safety:id/et_post").set_text("区域人" + self.yqm)
                # 确定按钮
                self.d(resourceId="cn.sqm.citymine_safety:id/tv_confirm").click()
            else:
                print("老用户登录！")
        except Exception as e:
            print(e)
        sleep(0.5)
        # 首次整改
        # 进入任务
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        # 点击待整改
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_waiting_for_rectification").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        # 整改：已整改:0、不能整改:1
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