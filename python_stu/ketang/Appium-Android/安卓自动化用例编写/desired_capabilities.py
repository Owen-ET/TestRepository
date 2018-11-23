#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 11:49
# @Author  : zc
# @File    : desired_capabilities.py


def get_desired_capabilities():
    desired_caps = {
  "platformName": "android",
  "deviceName": "xxx",
  "appPackage": "com.example.android.apis",
  "appActivity": ".ApiDemos"
}
    return desired_caps

def get_uri():
    return 'http://localhost:4723/wd/hub'