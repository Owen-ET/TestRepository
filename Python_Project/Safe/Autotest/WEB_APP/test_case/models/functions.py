#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/28 14:52
# @Author  : zc
# @File    : functions.py

import os
import configparser
from Autotest.WEB_APP.test_case.models import PyMysql,login


class AllFuncions(object):


    def screenshot(self,driver,imgName):
        '''
        截图方法
        :param driver:  启动浏览器
        :param imgName: 图片名称
        :return:    截图
        '''
        # 获取路径
        dir = os.path.dirname(os.path.dirname(__file__))
        # 设置基础路径
        base_dir = dir.split('test_case')[0]
        # 设置截图路径
        img_dir = base_dir + "report/img/" + imgName + ".png"
        # 截图
        driver.get_screenshot_as_file(img_dir)


    def select_sql(self,select_sql):
        '''
        查询数据库
        :param select_sql:  sql语句
        :return:            查询结果
        '''
        flag = 1

        return PyMysql.selectTable(select_sql, None, flag)


    def getNewName(self,name):
        '''
        get到新名字
        :param name:    原来的名
        :return:        newName
        '''

        '''SQL'''
        # 查询区域用户名、真实姓名SQL语句
        selectQYName_sql = "select user_username,user_realname from base_user " \
                           "where user_username like 'zcqy%' order by user_username desc limit 0,1"
        # 查询监察用户名、真实姓名SQL语句
        selectJCName_sql = "select user_username,user_realname from base_user " \
                           "where user_username like 'zcjc%' order by user_username desc limit 0,1"

        jc = self.jcPerson()
        list = [jc[0], jc[1]]
        if name in list:
            # 查询最新的监察用户名、真实姓名
            sql = self.select_sql(selectJCName_sql)
            if sql == None:
                newName = name + "1"
                return newName,"1"
            else:
                pass
        else:
            qy = self.qyPerson()
            list = [qy[0], qy[1]]
            # 查询最新的区域用户名、真实姓名
            sql = self.select_sql(selectQYName_sql)
            if sql == None:
                newName = name + "1"
                return newName,"1"
            else:
                pass

        # 原来的名字
        oldName = sql[list.index(name)]
        # 原来的数
        oldNum = str(oldName).split(name)[1]
        # 新的数
        newNum = int(oldNum) + 1
        # 新的名字
        newName = name + str(newNum)

        return newName,newNum,oldName,oldNum


    def getNewPhoneNum(self):
        '''
        get到新手机号
        :return:    newPhoneNum
        '''

        '''SQL'''
        # 查询手机号SQL语句
        selectPhoneNum_sql = "select user_phone from base_user " \
                             "where user_username like 'zc%' ORDER BY user_phone DESC LIMIT 0,1"

        # 查询最新的手机号
        sql = self.select_sql(selectPhoneNum_sql)
        if sql == None:
            newPhoneNum = "13642012301"
            return newPhoneNum
        else:
            pass
        newPhoneNum = int(sql[0]) + 1

        return newPhoneNum


    def getNewPwd(self,flag):
        '''
        get到最新用户名密码
        :return:
        '''

        if flag == self.jcPerson()[0]:
            '''SQL'''
            # 查询最新用户名密码SQL语句
            selectPwd_sql = "select user_pwd from base_user " \
                            "where user_username like  'zcjc%' ORDER BY user_username DESC LIMIT 0,1"
        elif flag == self.qyPerson()[0]:
            '''SQL'''
            # 查询最新用户名密码SQL语句
            selectPwd_sql = "select user_pwd from base_user " \
                            "where user_username like  'zcqy%' ORDER BY user_username DESC LIMIT 0,1"

        # 查询最新用户名密码
        pwd = self.select_sql(selectPwd_sql)
        if pwd[0] == '':
            return None
        else:
            return pwd[0]


    def getSynergetic(self):
        '''
        get到协同人员
        :return:
        '''

        '''SQL'''
        # 查询出数据库中的协同人员SQL语句
        selectSyn_sql = "select u.user_realname from " \
              "(select user_realname,renwu,organization_chart_id from base_user " \
              "where renwu like '%2%') as u " \
              "left join " \
              "(select organization_chart_id,organization_chart_name from organization_chart " \
              "where organization_chart_name like '%检查%') as o " \
              "on u.organization_chart_id=o.organization_chart_id " \
              "where o.organization_chart_id > 0"

        # 查询出数据库中的协同人员
        sql = self.select_sql(selectSyn_sql)
        if sql[0] == '':
            return None
        else:
            return sql[0]


    def jcPerson(self):
        '''
        监察人员参数
        :return: jc
        '''
        cf = configparser.ConfigParser()
        cf.read(login.configUrl())
        jc_name = cf.get("db", "jc_name")
        jc_realname = cf.get("db", "jc_realname")
        jc = [jc_name, jc_realname]

        return jc


    def qyPerson(self):
        '''
        区域人员参数
        :return: qy
        '''
        cf = configparser.ConfigParser()
        cf.read(login.configUrl())
        qy_name = cf.get("db", "qy_name")
        qy_realname = cf.get("db", "qy_realname")
        qy = [qy_name, qy_realname]

        return qy