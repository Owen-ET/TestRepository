#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 11:51
# @Author  : zc
# @File    : main.py


from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import unittest
from time import sleep
import Safe.Autotest.Appium.Android.desired_capabilities as desired_capabilities
from selenium.webdriver.common.by import By



class AndroidTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        desired_cap = desired_capabilities.get_desired_capabilities()
        uri = desired_capabilities.get_uri()
        self.d = webdriver.Remote(uri,desired_cap)


    @classmethod
    def tearDownClass(self):
        sleep(10)
        # self.d.quit()
        pass


    def setUp(self):
        print("=======start!=======")
        sleep(5)
        self.size = self.d.get_window_size()
        print(self.size)
        self.halfWidth = self.size['width']/2
        # 输入用户名
        userName = self.d.find_element(By.ID,"cn.sqm.citymine_safety:id/et_login_id")
        userName.send_keys("xxx")
        # 输入密码
        password = self.d.find_element(By.ID,"cn.sqm.citymine_safety:id/et_login_password")
        password.send_keys("xxx")
        # 登录密码
        button = self.d.find_element(By.ID,"cn.sqm.citymine_safety:id/btn_login")
        button.click()


    def tearDown(self):
        print("=======stop!=======")


    def test1(self):
        print("测试开始！")
        sleep(2)
        # 发起任务
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/rl_add_task").click()
        # 任务类型
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/tv_select_task_type").click()
        self.d.swipe(self.halfWidth, 1630, self.halfWidth, 1530, 500)
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/btn_confirm").click()
        # 检查区域
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/tv_select_inspection_area").click()
        self.d.find_elements_by_id("cn.sqm.citymine_safety:id/item_tv_department")[0].click()
        # 隐患类型
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/tv_select_hidden_danger_type").click()
        for i in range(2):
            self.d.swipe(self.halfWidth,1630,self.halfWidth,1530)
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/btn_confirm").click()
        # 隐患描述：手机必须设置Appium输入法
        # self.d.find_element_by_android_uiautomator("new UiSelector().text(\"请输入内容\")").send_keys("安全隐患")
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/et_hidden_danger_description").send_keys("安全隐患")
        # 照片
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/iv_choose_photos").click()
        # text定位
        self.d.find_element_by_android_uiautomator("new UiSelector().text(\"手机相册\")").click()
        self.d.find_elements_by_id("cn.sqm.citymine_safety:id/v_selected")[4].click()
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/done").click()
        # 违反制度管理
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/iv_add_violation").click()
        self.d.find_element_by_android_uiautomator("new UiSelector().text(\"易燃易爆危险物品和场所防火防暴管理制度\")").click()
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/tv_complete").click()
        # 向上拖动
        sleep(0.5)
        self.d.swipe(self.halfWidth, 1490, self.halfWidth, 120, 500)
        # 整改期限
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/tv_please_the_rectification_date").click()
        for i in range(2):
            self.d.swipe(900,1622,900,1530)
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/btn_confirm").click()
        # 协同人员
        list = self.d.find_elements_by_id("cn.sqm.citymine_safety:id/item_tv_personnel_name")
        num = len(list)
        list[num-num].click()
        self.d.find_element_by_android_uiautomator("new UiSelector().text(\"xxx\")").click()
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/tv_complete").click()
        # 区域负责人
        list = self.d.find_elements_by_id("cn.sqm.citymine_safety:id/item_tv_personnel_name")
        num = len(list)
        list[num-1].click()
        for i in range(2):
            self.d.find_element_by_id("cn.sqm.citymine_safety:id/lv_area_manager").click()
        self.d.find_element_by_android_uiautomator("new UiSelector().text(\"xxx\")").click()
        self.d.find_element_by_id("cn.sqm.citymine_safety:id/tv_complete").click()
        # 提交
        # self.d.find_element_by_id("cn.sqm.citymine_safety:id/btn_submit").click()


        # 断言
        text = self.d.find_element_by_android_uiautomator("new UiSelector().text(\"违反制度管理\")").text
        self.assertEqual(text,"违反制度管理1","显示不对！")



    # def leftSwipe(self):
    #     window_size = self.driver.get_window_size()
    #     self.driver.swipe(start_x=window_size["width"] * 0.8,
    #                       start_y=window_size["height"] * 0.5,
    #                       end_x=window_size["width"] * 0.1,
    #                       end_y=window_size["height"] * 0.5 )
    #
    # def wait_for_element(self,xpath=None, id=None, index=None, timeOut=20):
    #     startTime = time.time()
    #     nowTime = time.time()
    #     while nowTime - startTime < timeOut:
    #         try:
    #             if xpath is not None:
    #                 el = self.driver.find_element_by_xpath(xpath)
    #                 return el
    #         except:
    #             pass
    #
    #         try:
    #             if id is not None:
    #                 if index is not None:
    #                     return self.driver.find_element_by_id(id)[index]
    #                 else:
    #                     return self.driver.find_element_by_id(id)
    #         except:
    #             pass
    #
    #         sleep(1)
    #
    #         nowTime = time.time()
    #
    #     raise Exception("Element xpath[%s] id[%s] index[%s] is not found" % (xpath, id, index))
    #
    #
    # def test_a_utFrame(self):
    #
    #     print(self.driver.current_activity)
    #     self.wait_for_element(id="com.ut.androidtest:id/downloadBtn").click()
    #
    #     time.sleep(8)
    #     circulation = 2
    #
    #     while circulation > 0:
    #         time.sleep(1)
    #         self.leftSwipe()
    #         self.leftSwipe()
    #
    #
    #         self.wait_for_element(xpath="//*[@text='欢迎使用']").click()
    #         time.sleep(1)
    #
    #         loginBtn = self.wait_for_element(xpath="//*[@text='登    录']")
    #         loginBtn.click()
    #         time.sleep(1)
    #
    #         self.wait_for_element(xpath="//*[@text='XX申请']").click()
    #         time.sleep(1)
    #
    #         item = self.wait_for_element(xpath="//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]")
    #         item.click()
    #         time.sleep(1)
    #
    #
    #         backBtn = self.wait_for_element(id="com.ut.androidtest:id/imageTextBt_imageBt")
    #         backBtn.click()
    #         time.sleep(.5)
    #
    #         #系统返回键
    #         self.driver.press_keycode(keycode=4)
    #         time.sleep(1)
    #
    #         self.wait_for_element(xpath="//*[@text='日志查询']").click()
    #         time.sleep(1.5)
    #
    #         self.wait_for_element(xpath="//*[@text='录像日志']").click()
    #         self.wait_for_element(xpath="//*[@text='领用日志']").click()
    #         self.wait_for_element(xpath="//*[@text='归还日志']").click()
    #         self.wait_for_element(xpath="//*[@text='报警日志']").click()
    #         time.sleep(.5)
    #
    #         self.wait_for_element(xpath="//*[@text='消息']").click()
    #         self.wait_for_element(xpath="//*[@text='首页']").click()
    #         self.wait_for_element(xpath="//*[@text='我']").click()
    #         time.sleep(1)
    #
    #         updateBtn = self.wait_for_element(xpath="//*[@text='版本更新']")
    #         updateBtn.click()
    #         time.sleep(10)
    #
    #         self.assertIsNotNone(self.wait_for_element(xpath="//*[@text='Hello world']"), "版本更新失败")
    #
    #         circulation -= 1




if __name__=='__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(AndroidTest("test1"))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()