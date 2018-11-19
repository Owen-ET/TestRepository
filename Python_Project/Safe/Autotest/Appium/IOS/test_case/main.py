#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 11:51
# @Author  : zc
# @File    : main.py


from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from Safe.Autotest.Appium.IOS.models.functions import Functions
import Safe.Autotest.Appium.IOS.desired_capabilities as desired_capabilities
import unittest


class AndroidTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        desired_cap = desired_capabilities.get_desired_capabilities()
        uri = desired_capabilities.get_uri()
        # 启动app
        self.d = webdriver.Remote(uri,desired_cap)


    @classmethod
    def tearDownClass(self):
        sleep(10)
        # self.driver.quit()
        pass


    def setUp(self):
        print("=======start!=======")
        sleep(2)
        self.size = self.d.get_window_size()
        self.half_Width = self.size['width']/2
        # 输入用户名
        userName = self.d.find_element(By.CLASS_NAME,"XCUIElementTypeTextField")
        userName.send_keys("xxx")
        # 隐藏键盘
        self.d.find_element_by_accessibility_id("login_bg_top").click()
        # 输入密码
        password = self.d.find_element(By.CLASS_NAME,"XCUIElementTypeSecureTextField")
        password.send_keys("xxx")
        # 隐藏键盘
        self.d.find_element_by_accessibility_id("login_bg_top").click()
        # 登录密码
        button = self.d.find_element_by_accessibility_id("登录")
        button.click()


    def tearDown(self):
        print("=======stop!=======")


    def do_swipe(self,x1,y1,x2,y2):
        '''
        # 滑动方法
        :return:
        '''
        self.d.execute_script("mobile: dragFromToForDuration",
                              {"fromX": x1, "fromY": y1, "toX": x2, "toY": y2, "duration": 0.5})


    def isClick(self,i):
        '''
        # 判断可不可以点击元素
        :param i:
        :return:
        '''
        try:
            print("判断：[%s]，可不可以点击" % i)
            self.d.find_element_by_name(i).click()
            return True
        except:
            return False


    def test1(self):
        print("测试开始！")
        # 发起任务
        self.d.find_element_by_name("home btn newtask").click()
        # 任务类型
        self.d.find_elements_by_name("home arrow news")[0].click()
        self.do_swipe(160,450,160,400)
        self.d.find_element_by_name("确定").click()
        # 检查单位
        self.d.find_elements_by_name("home arrow news")[1].click()
        self.d.find_element_by_xpath('//XCUIElementTypeStaticText[@name="基地"]').click()
        # 隐患类型
        self.d.find_elements_by_name("home arrow news")[2].click()
        for i in range(2):
            self.do_swipe(self.half_Width,470,self.half_Width,435)
        self.d.find_element_by_name("确定").click()
        # 隐患描述
        self.d.find_element_by_accessibility_id("请输入内容").send_keys("安全")
        self.d.find_element_by_name("隐患描述").click()
        # 照片
        self.d.find_element_by_accessibility_id("addtask btn add pic").click()
        for i in range(4):
            self.do_swipe(self.half_Width,350,15,350)
        self.d.find_elements_by_name("btn unselected")[1].click()
        self.d.find_element_by_name("确定(1)").click()
        # 违反管理制度
        self.d.find_element_by_accessibility_id("addtask btn add file").click()
        sleep(2)
        list = ["叉车操作安全管理制度","员工行为管理规范","易燃易爆危险物品和场所防火防暴管理制度"]
        for i in list:
            print(i)
            if self.isClick(i):
                print("已选择：[%s]"%i)
            else:
                print("选择不到：[%s]，向下滚动"%i)
                # 向下滚动
                self.d.execute_script('mobile:scroll', {'direction': 'down'})
                if self.isClick(i):
                    print("已选择：[%s]"%i)
                else:
                    print("选择不到：[%s]，向上滚动"%i)
                    # 向上滚动
                    self.d.execute_script('mobile:scroll', {'direction': 'up'})
                    self.d.find_element_by_name(i).click()
                    print("已选择：[%s]" % i)
        # 返回
        self.d.find_element_by_name("login btn back").click()
        # 拖动到最下面
        self.d.execute_script('mobile:scroll', {'direction': 'down'})
        # 整改期限
        self.d.find_elements_by_name("home arrow news")[3].click()
        self.do_swipe(230,470,230,430)
        self.d.find_element_by_name("确定").click()
        # 协同人员
        self.d.find_elements_by_name("addtask btn add people")[0].click()
        self.d.find_element_by_name("xxx").click()
        self.d.find_element_by_name("login btn back").click()
        # 区域负责人
        self.d.find_elements_by_name("addtask btn add people")[1].click()
        self.d.find_element_by_name("xxx").click()
        self.d.find_element_by_name("login btn back").click()
        # 提交
        self.d.find_element_by_accessibility_id("提交").click()


        # 断言
        text = self.d.find_element_by_accessibility_id("违反制度管理").text
        print(text)
        self.assertEqual(text,"违反制度管理","显示不对！")


if __name__=='__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(AndroidTest("test1"))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()