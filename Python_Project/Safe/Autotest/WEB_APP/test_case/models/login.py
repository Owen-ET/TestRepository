#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/05 10:19
# @Author  : zc
# @File    : login.py

import requests
import configparser
import os

import json
import base64
from Crypto.Hash import MD5
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def encrypt_rsa(payload):
    x = json.dumps(payload,sort_keys=True)
    # 秘钥
    hash = MD5.new()
    hash.update(x.encode())
    key = hash.hexdigest()[0:16]
    aes = AES.new(key.encode(), AES.MODE_ECB)
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    message = pad(x).encode()
    # 先进行aes加密
    encrypt_aes = aes.encrypt(message)
    # 用base64转成字符串形式
    aes_text = base64.b64encode(encrypt_aes).decode('utf8')
    #rsa 加密aes秘钥
    message = key.encode()
    modulus = 99437084381349685477276313394303170573433886677562731860781240811787660470689217290670744707194263202395078373555860378773072630591263356037631691178750057709186517536630049206804629757937103683341803248104620635950209101746929261883751538295945103766784311780525325530567846111945662216393713939808104905017
    exponent = 65537
    rsa_pubkey = RSA.construct((modulus, exponent))
    f = open('./mykey.pem','w')
    f.write(rsa_pubkey.export_key().decode('utf8'))
    f.close()
    f = open('./mykey.pem', 'r')
    rsakey = RSA.importKey(f.read())
    cipher = PKCS1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message)).decode('utf8')
    return aes_text,cipher_text


def cookie_value(url,username,password):
    '''
    返回cookie:value
    :param url: 地址
    :param username: 用户名
    :param password: 密码
    :return: cookie：value
    '''
    payload = {'username':username,'pwd':password}
    r = requests.post(url=url,data=payload)
    return r.cookies['PHPSESSID']


def configUrl():
    '''
    配置文件绝对路径
    :return:configdir
    '''
    dir = os.path.abspath(os.path.dirname(__file__))
    configdir = dir + "/config.ini"
    return configdir


def mlogin():
    '''
    生产登录函数
    :return:【cookie】：value
    '''
    cf = configparser.ConfigParser()
    cf.read(configUrl())
    baseurl = cf.get("db", "baseurl")
    url = baseurl + "/Admin/Account/loginupdate.html"
    m_user = cf.get("db", "m_user")
    m_pass = cf.get("db", "m_pass")
    return cookie_value(url,m_user,m_pass)


def rlogin():
    '''
    回收登录函数
    :return:【cookie】：value
    '''
    cf = configparser.ConfigParser()
    cf.read(configUrl())
    baseurl = cf.get("db", "baseurl")
    url = baseurl + "/Admin/Account/loginupdate.html"
    r_user = cf.get("db","r_user")
    r_pass = cf.get("db","r_pass")
    return cookie_value(url,r_user,r_pass)


def safeLogin():
    '''
    小卖安全登录函数
    :return:
    '''
    cf = configparser.ConfigParser()
    cf.read(configUrl())
    safeBaseUrl = cf.get("db", "safeurl")
    url = safeBaseUrl
    safe_user = cf.get("db", "safe_user")
    safe_pass = cf.get("db", "safe_pass")
    return cookie_value(url,safe_user,safe_pass)


def jlogin():
    '''
    加盟商登录函数
    :return: Authorization
    '''
    cf = configparser.ConfigParser()
    cf.read(configUrl())
    appbaseurl = cf.get("db", "appbaseurl")
    url = appbaseurl + ":8082/appJoinUser/user/login"
    j_user = cf.get("db", "j_user")
    j_pass = cf.get("db", "j_pass")
    encrypt = encrypt_rsa({'telephone': j_user, 'password': j_pass})
    payload = {'search': encrypt[0], 'signature': encrypt[1]}
    r = requests.post(url=url, data=payload)
    return r.headers['Authorization']


def slogin():
    '''
    供货商登录函数
    :return: Authorization
    '''
    cf = configparser.ConfigParser()
    cf.read(configUrl())
    appbaseurl = cf.get("db", "appbaseurl")
    url = appbaseurl + ":8082/supplyAppUser/user/login"
    s_user = cf.get("db", "s_user")
    s_pass = cf.get("db", "s_pass")
    encrypt = encrypt_rsa({'telephone': s_user, 'password': s_pass})
    payload = {'search': encrypt[0], 'signature': encrypt[1]}
    r = requests.post(url=url, data=payload)
    return r.headers['Authorization']