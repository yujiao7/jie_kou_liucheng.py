#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/12'
from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool

import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf



d ={}
d["userName"]= "stp74699"
@allure.title("注册接口")
def test_change_pwd_var():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/signup'

    req = {
  "phone": "13968531499",
  "pwd": "striy3322",
  "rePwd": "striy3322",
  "userName": d["userName"]
}


    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    allure.attach("预期结果:{},实际结果:{}".format(200, resp.status_code), "响应状态码断言", allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(2000,body['code']),"响应code",allure.attachment_type.TEXT)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)


@allure.title("登录接口")
def test_change_pwd_denglu():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/login'

    req = {
  "pwd": "striy3322",
  "userName": d["userName"]
}


    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    d['token'] = body['data']['token']
    # 判断响应码
    allure.attach("预期结果:{},实际结果:{}".format(200, resp.status_code), "响应状态码断言", allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(2000,body['code']),"响应code",allure.attachment_type.TEXT)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)


@allure.title("修改密码")
def test_change_pwd():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/user/changepwd'

    req = {
  "newPwd": "striy33223",
  "oldPwd": "striy3322",
  "reNewPwd": "striy33223",
  "userName": d["userName"]
}

    aaa ={'token':d['token']}
    resp = request_tool.post_request(url, json=req,headers=aaa)
    body = resp.json()
    # 判断响应码
    allure.attach("预期结果:{},实际结果:{}".format(200, resp.status_code), "响应状态码断言", allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(2000,body['code']),"响应code",allure.attachment_type.TEXT)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)








