#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 11:49
# @Author  : zc
# @File    : desired_capabilities.py


def get_desired_capabilities():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "OPPO",
        "appPackage": "cn.sqm.citymine_safety",
        "appActivity": ".activity.LauncherActivity",
        "udid": "608ad0fe",
        "unicodeKeyboard": True,
        "resetKeyboard": True
        # 'appWaitActivity': ".LoginActivity"
    }
    return desired_caps

def get_uri():
    return 'http://localhost:4723/wd/hub'