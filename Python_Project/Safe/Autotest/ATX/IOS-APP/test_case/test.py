#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 11:42
# @Author  : zc
# @File    : test.py


import unittest
import wda
from time import sleep


class Test_safety(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        wda.DEBUG = False # default False
        wda.HTTP_TIMEOUT = 10.0 # default 60.0 seconds
        cls.c = wda.Client('http://localhost:8100')

        # cls.e = wda.Element().clear_text()
        cls.c.healthcheck()  # 解锁屏幕并启动uiautomator服务
        # cls.c.toast.show("测试开始", 1.5)
        cls.c.home()

    @classmethod
    def tearDownClass(cls):
        # cls.c.toast.show("测试结束", 2)
        # cls.c.app_stop_all()
        # cls.c.service("WebDriverAgent").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行
        pass

    def setUp(self):
        print("=======start!=======")
        bundle_id = "com.chen.CityMineSafetyOne"
        # # 清除数据
        # self.c.app_clear(bundle_id)
        # 启动应用
        self.s = self.c.session(bundle_id)
        # 密码登录元素
        pwdLogin = self.s(name='密码登录',className='Button')
        # 判断元素存不存在
        if pwdLogin.exists:
            # 输入用户名
            self.s(type='TextField').tap()
            self.s(type='TextField').clear_text()
            self.s(type='TextField').set_text("zcjc1")
            self.s(name='收起键盘',className='Button').tap()
            # 输入密码
            self.s(type='SecureTextField').tap()
            self.s(type='SecureTextField').clear_text()
            self.s(type='SecureTextField').set_text("111111")
            self.s(name='login_bg_top', className='Image').tap()
            # 点击登录按钮
            self.s(name='登录',className='Button').tap()
            sleep(0.5)
        else:
            print("直接进入首页")
            pass


    def tearDown(self):
        print("=======stop!=======")
        # self.s.close() # 关闭应用
        pass

    def test1(self):
        # 获取屏幕大小
        size = self.s.window_size()
        # 点击发起任务
        self.s(name='home btn newtask',className='Button').tap()
        sleep(1)
        # 任务类型
        self.s(name=u"home arrow news",index=1).tap()
        self.s.swipe(size[0]*0.5, size[1]*0.8, size[0]*0.5, size[1]*0.72, 0.5)
        self.s(name='确定',className='Button').tap()
        # 检查单位
        self.s(name=u"home arrow news",index=2).tap()
        self.s(name=u"下一级", index=1).tap()
        self.s(name='区域1', className='StaticText').tap()
        # 隐患类型
        self.s(name=u"home arrow news", index=3).tap()
        self.s.swipe(size[0]*0.5, size[1]*0.8, size[0]*0.5, size[1]*0.72, 0.5)
        self.s(name='确定', className='Button').tap()
        # 隐患描述
        self.s(type="TextView").set_text("交通违法！")
        self.s(name='收起键盘', className='Button').tap()
        # 照片
        self.s(name='照片').tap()
        for i in range(4):
            self.s.swipe(size[0]*0.55, size[1]*0.6, size[0]*0, size[1]*0.6)
        self.s(label=u"btn unselected", name=u"btn unselected", type="Button", index=1).tap()
        self.s(name='确定(1)', className='Button').tap()
        # 违反制度管理
        self.s(name='违反制度管理').tap()
        wfzdList = ['违反消防相关制度','违反员工行为规范']
        for i in wfzdList:
            self.s(name=i).tap()
        self.s(label=u"login btn back").tap()
        # 拖到底部
        self.s.swipe(size[0]*0.5,size[1]*0.85,size[0]*0.5,size[1]*0.12)
        # 整改期限
        self.s(name=u"home arrow news", index=4).tap()
        self.s.swipe(size[0]*0.75,size[1]*0.82,size[0]*0.75,size[1]*0.766)
        self.s(name='确定', className='Button').tap()
        # 协同人员
        self.s(label=u"addtask btn add people",index=1).tap()
        self.s(name='jiancha1').tap()
        self.s(label=u"login btn back").tap()
        # 区域负责人
        self.s(label=u"addtask btn add people",index=2).tap()
        self.s(name='zc区域1').tap()
        self.s(label=u"login btn back").tap()

        # 断言
        btn = self.s(label=u"提交").text
        self.assertEqual(btn,"提交","按钮名字错误！")
        # 提交按钮
        sleep(2)

if __name__ == '__main__':
    unittest.main()