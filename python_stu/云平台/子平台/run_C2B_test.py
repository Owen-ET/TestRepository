#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 17:21
# @Author  : zc
# @File    : run_C2B_test.py


import os
import time
import unittest
import yagmail
from BSTestRunner import BSTestRunner
from selenium import webdriver
from time import sleep
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.text import MIMEText



def openFile(report_file):
    '''
    打开测试报告
    :param report_file:
    :return:
    '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    address = "file:///" + report_file
    driver.get(address)
    sleep(10)


def getNewReport(report_url):
    '''
    获取最新生成的测试报告
    :param report_url:
    :return:
    '''
    lists = os.listdir(report_url)
    lists.sort(key= lambda fn: os.path.getmtime(report_url + fn))
    newReport = os.path.join(report_url,lists[-1])
    return newReport


def sendMail(newReport,report_name):
    '''
    ①普通发送邮件
    :param newReport:
    :param report_name:
    :return:
    '''
    sendMail = 'xxx@126.com'
    sendpswd = 'xxx'
    receiveMail = 'xxx@qq.com'


    # 创建邮件信息
    msg = MIMEMultipart()
    # 读取最新报告文件
    f = open(newReport,'rb').read()
    # 设置邮件主体
    mailBody =  MIMEText(f,'html','utf-8')
    # 邮件主体放入到消息中
    msg.attach(mailBody)
    # 邮件标题
    msg['Subject'] = Header("《自动化测试报告邮件》",'utf-8')
    msg['From'] = sendMail
    msg['To'] = receiveMail

    # 邮件附件
    att = MIMEApplication(f)
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition','attachment',filename=report_name)
    msg.attach(att)


    smtp = SMTP()
    # 连接邮箱
    smtp.connect('smtp.126.com')
    # 邮箱登录
    smtp.login(sendMail,sendpswd)
    # 发送邮件
    smtp.sendmail(sendMail,receiveMail,msg.as_string())


def sendYagMail(newReport,report_file):
    '''
    ②用yagmail发送邮件
    :return:
    '''

    sendMail = 'xxx@126.com'
    sendpswd = 'xxx'
    receiveMail = 'xxx@qq.com'

    # 连接邮箱服务器
    yag = yagmail.SMTP(user=sendMail, password=sendpswd, host='smtp.126.com')
    # 普通邮件正文
    contents = ['第一段', '自动化', '报告邮件']

    # 编辑邮件
    # 读取邮件模板
    file_object = open(newReport)
    try:
        contentsbody = file_object.read()
    finally:
        file_object.close()

    contents = contentsbody

    # 附件地址
    fujian = [report_file]
    # 发送邮件附件
    yag.send(receiveMail, '《自动化测试报告》', contents, fujian)





if __name__ == '__main__':

    # 基础路径
    base_url = os.path.dirname(os.path.abspath(__file__))
    print(base_url)
    # 用例路径
    case_url = base_url + "/WEB/test_case/"
    # 报告路径
    report_url = base_url + "/WEB/report/"
    # 文件名称
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    report_name = now + "_report.html"
    # 报告文件
    report_file = report_url + report_name
    # 创建报告文件并写入
    fp = open(report_file,'wb')

    # 运行用例
    discover = unittest.defaultTestLoader.discover(case_url,
                                                   pattern='test*.py')
    # 生成测试报告并写在BSTestRunner中
    runner = BSTestRunner(stream=fp,
                          title='自动化测试报告：',
                          description='执行测试用例的结果：')

    # 用例结果反馈到报告中
    runner.run(discover)
    fp.close()
    # 打开测试报告
    openFile(report_file)

    # 获取最新的report文件
    newReport = getNewReport(report_url)

    # ①普通发送邮件正文及附件
    # sendMail(newReport,report_name)

    # ②用yagmail发送邮件（推荐）
    sendYagMail(newReport,report_file)