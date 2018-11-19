#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 14:07
# @Author  : zc
# @File    : 网易云音乐.py


import wda





bundle_id = 'com.netease.cloudmusic'

c = wda.Client('http://localhost:8100') # DEVICE_URL

s = c.session(bundle_id) # 启动应用

# 处理不知何时就会突然弹出的警告框
def alert_callback(session):
    btns = set([u'不再提醒', 'OK', u'知道了', 'Allow', u'允许']).intersection(session.alert.buttons())
    if len(btns) == 0:
        raise RuntimeError("Alert can not handled, buttons: " + ', '.join(session.alert.buttons()))
    session.alert.click(list(btns)[0])

s.set_alert_callback(alert_callback)


def netease_login(s):
    # 已经登录直接跳过
    # 开头有2s的广告，所以这里需要等待3s
    if s(name=u'发现音乐', type='Button').wait(3, raise_error=False):
        # Already logged in
        return
    # 点击邮箱登录，输入帐号密码，验证是否登录成功
    s(name=u'网易邮箱').tap()
    s(type='TextField').set_text(USERNAME+'\n')
    s(type='SecureTextField').set_text(PASSWORD+'\n')
    s(name=u'开启云音乐').click_exists(timeout=3.0)
    assert s(name=u'发现音乐', type='Button').wait(5.0) # 等待5s

netease_login(s)


def setup_function():
    # 每次测试之前，保证帐号是登录的
    s = c.session(bundle_id)
    netease_login(s)

def teardown_function():
    s.close() # 一次测试结束，关闭应用

def test_discover_music():
    """
    测试 发现音乐->私人FM 中的播放功能
    """
    s(name=u'发现音乐', type='Button').tap() # 默认会寻找10s，所以不用担心点不到
    assert s(name=u'听歌识曲', visible=True).wait()
    s(name=u'私人FM').tap()
    assert s(name=u'不再播放').exists
    assert s(name=u'添加到我喜欢的音乐').exists
    assert s(name=u'00:00', className='StaticText').exists
    s(nameMatches=u'(暂停|播放)').tap() # 点击播放后，按钮会变成暂停，这里用正则匹配下
    assert s(name=u'00:00', className='StaticText').wait_gone(10.0) # 等待音乐播放，进度条开始走了

def test_my_music():
    """
    测试 我的音乐->本地音乐
    """
    s(name=u'我的音乐', type='Button').tap()
    assert s(name=u'最近播放').wait(2.0)
    s(name=u'本地音乐').tap()
    assert s(name=u'管理').wait()
    s(name=u'播放全部').tap()

