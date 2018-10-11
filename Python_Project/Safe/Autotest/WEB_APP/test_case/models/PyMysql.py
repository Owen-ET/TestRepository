#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/21 09:20
# @Author  : zc
# @File    : PyMysql.py

import pymysql


def connectMysql():
    '''connectMysql
    连接Mysql数据库
    :return: db
    '''
    # 连接配置信息
    config = {
         'db' : "sqmjc",                                                # 数据库
         'host' : "rm-3xevi3kefz7sby600fo.mysql.rds.aliyuncs.com",      # 主机192.168.2.40
         'port' : 3306,                                                 # 端口
         'user' : "super",                                              # 用户名
         'password' : "CITY2018@mine"                                   # 密码
    }

    # 创建连接
    db = pymysql.connect(**config)
    # 返回数据库
    return db


def selectTable(sql,args,flag):
    '''
    # 1.查询操作
    :return:查询表et01数据
    '''
    # 获取操作游标
    cur = connectMysql().cursor()
    try:
        if flag == 1:
            cur.execute(sql)                # 执行sql语句
            results = cur.fetchall()        # 获取查询的所有记录
            # 遍历结果
            for row in results:
                return row
        else:
            cur.executemany(sql, args)      # 执行sql语句
            results = cur.fetchall()        # 获取部分查询的记录
            for row in results:
                print(row[0])
    except Exception as e:
        raise e
        print("raise后，会不会执行！")

    finally:
        connectMysql().close()              # 关闭连接


def publicMethods(sql,args):
    '''
    # 2.增、删、改操作
    :return:
    '''
    db = connectMysql()
    # 获取操作游标
    cur = db.cursor()
    try:
        # 对多条数据进行操作
        cur.executemany(sql,args)
        # 提交
        db.commit()
    except:
        # 错误回滚
        db.rollback()
    finally:
        cur.close()
        db.close()