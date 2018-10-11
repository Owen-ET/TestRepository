#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/08/31 09:43
# @Author  : zc
# @File    : test_01监察人员_首次发起整改.py

import uiautomator2 as u2
import unittest
from time import sleep
from Autotest.WEB_APP.test_case.models.functions import AllFuncions


class TestMineSafe(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb('608ad0fe')
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        cls.u.toast.show("test_01监察人员_首次发起整改,测试开始", 1.5)


    @classmethod
    def tearDownClass(cls):
        cls.u.toast.show("test_01监察人员_首次发起整改,测试结束", 2)
        cls.u.app_stop_all()
        cls.u.service("uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行


    def setUp(self):
        # 清除数据
        self.u.app_clear("cn.sqm.citymine_safety")
        # 启动小卖安全
        self.d = self.u.session("cn.sqm.citymine_safety")  # restart app
        sleep(0.2)
        # 允许获取位置信息
        try:
            self.d.implicitly_wait(4.5)
            if self.d(resourceId="android:id/alertTitle").exists:
                print("新版本获取位置信息！")
                self.d(resourceId="android:id/button1").click()
            else:
                print("老版本不获取位置信息！")
        except Exception as e:
            print(e)

        # 判断密码存不存在
        zcjc = AllFuncions().jcPerson()
        fu = AllFuncions().getNewPwd(zcjc[0])
        username = AllFuncions().getNewName(zcjc[0])[2]
        self.realname = AllFuncions().getNewName(zcjc[1])[2]
        newPwd = "111111"
        if fu != None:
            '''密码登录'''
            print("密码登录")
            # 输入用户名
            #TODO
            self.d(resourceId="cn.sqm.citymine_safety:id/et_login_id").click()
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
            self.yqm = AllFuncions().getNewName(zcjc[0])[3]
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
        pass


    def testLauReform(self):  # 发起任务
        '''测试用例03：首次发起整改'''
        #新用户登录：修改个人信息
        try:
            if self.d(text=u"修改个人信息").exists:
                print("新用户登录！")
                # 头像
                self.d(resourceId="cn.sqm.citymine_safety:id/img_header").click()
                self.d(text=u"手机相册").click()
                sleep(0.5)
                self.d.click(0.5, 0.15)
                sleep(0.5)
                self.d.click(0.6, 0.6)
                # 职务
                self.d(resourceId="cn.sqm.citymine_safety:id/et_post").set_text("监察人" + self.yqm)
                #确定按钮
                self.d(resourceId="cn.sqm.citymine_safety:id/tv_confirm").click()
            else:
                print("老用户登录！")
        except Exception as e:
            print(e)
        sleep(0.5)

        # 点击发起任务
        self.d(className="android.widget.ImageView", instance=10).click()
        # 选择任务类型：全部0、专项1、日常2、火灾3...
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_select_task_type").click()
        sleep(0.5)
        for i in range(0):
            self.d(className="android.view.View").drag_to(0.5, 0.8, duration=0.5)
        self.d(resourceId="cn.sqm.citymine_safety:id/btn_confirm").click()
        # 检查单位
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_select_inspection_area").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/item_tv_next_level").click()
        self.d(text='区域1').click()
        # 隐患类型:其他0、交通1、维稳2、火灾3
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_select_hidden_danger_type").click()
        for i in range(0):
            self.d(className="android.view.View").drag_to(0.5, 0.8, duration=0.5)
        self.d(text='确定').click()
        # 隐患描述
        self.d(resourceId="cn.sqm.citymine_safety:id/et_hidden_danger_description").set_text("其他,第一次发起！")
        self.d.click(0.9, 0.6)
        # 照片：
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_choose_photos").click()
        self.d(text=u"手机相册").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/button").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_dir_name", text=u"Camera").click()
        #TODO
        self.d(resourceId="cn.sqm.citymine_safety:id/v_selected", className="android.widget.ImageView", instance=11).click()
        self.d(resourceId="cn.sqm.citymine_safety:id/done").click()
        # 违反制度
        self.d(resourceId="cn.sqm.citymine_safety:id/iv_add_violation").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/item_tv_content_violation", text=u"其他").click()
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_complete").click()
        # 向上滑动拖拽
        self.d(className="android.widget.LinearLayout").drag_to(0.5, 0.00, duration=0.5)
        # 整改期限
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_please_the_rectification_date").click()
        for i in range(0):
            self.d(resourceId="cn.sqm.citymine_safety:id/day").drag_to(0.82, 0.8, duration=0.5)
        self.d(text='确定').click()
        # 协同人员
        list=[]
        list.append(AllFuncions().getSynergetic())
        self.d(resourceId="cn.sqm.citymine_safety:id/item_tv_personnel_name").click()
        for i in range(len(list)):
            self.d(resourceId="cn.sqm.citymine_safety:id/item_tv_personnel_name", text=list[i]).click()
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_complete").click()
        # 区域负责人
        self.d(resourceId="cn.sqm.citymine_safety:id/item_tv_personnel_name", className="android.widget.TextView",
          instance=len(list) + 1).click()
        for i in range(2):
            self.d(resourceId="cn.sqm.citymine_safety:id/lv_area_manager").click()
        #TODO
        # 选择对应的区域负责人
        zcqy = AllFuncions().qyPerson()[1]
        qyUser = AllFuncions().getNewName(zcqy)[2]
        self.d(resourceId="cn.sqm.citymine_safety:id/item_tv_department", text=qyUser).click()
        self.d(resourceId="cn.sqm.citymine_safety:id/tv_complete").click()
        sleep(0.5)
        # 提交按钮
        self.d(resourceId="cn.sqm.citymine_safety:id/btn_submit").click()
        sleep(0.5)


        #断言
        #点击【任务】栏
        self.d(resourceId="cn.sqm.citymine_safety:id/rb_task").click()
        #进入任务详情
        self.d(resourceId="cn.sqm.citymine_safety:id/rl_bg").click()
        #向上滑动
        self.d(resourceId="cn.sqm.citymine_safety:id/watermark").drag_to(0.5,0.15,duration=0.5)
        sleep(0.5)
        #验证监察人员
        text = self.d(resourceId="cn.sqm.citymine_safety:id/tv_superviser").get_text()
        print(text)
        #TODO
        self.assertEqual(text,self.realname,"监察人员姓名错误！")