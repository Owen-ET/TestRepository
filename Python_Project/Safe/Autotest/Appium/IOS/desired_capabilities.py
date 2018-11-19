#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 11:49
# @Author  : zc
# @File    : desired_capabilities.py


def get_desired_capabilities():
    desired_caps = {
        "platformName": "iOS",
        "platformVersion": "10.3.1",
        "deviceName": "iPhone5s",
        "bundleId": "com.chen.CityMineSafetyOne",
        "AutomationName": "XCUITest",
        "udid": "42ebab931b6b2d6a140b1a4f5bd55305dbfe2ff0",
        "NewCommandTimeout": "3600",
        # "useNewWDA": True,
        # "unicodeKeyboard": True,
        # "resetKeyboard": True
    }
    return desired_caps

def get_uri():
    return 'http://localhost:4723/wd/hub'