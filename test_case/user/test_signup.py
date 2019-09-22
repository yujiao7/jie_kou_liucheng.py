#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/11'
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
@allure.epic("商城后台系统")
@allure.feature("用户模块")
@allure.story("注册接口")
@allure.title("全字段正常流")
def test_change_pwd_var():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/signup'

    req = {
  "phone": "17764821231",
  "pwd": "yj123457",
  "rePwd": "yj123457",
  "userName": "yyjj012"
}


    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    allure.attach("预期结果:{},实际结果:{}".format(200, resp.status_code), "响应状态码断言", allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(2000,body['code']),"响应code",allure.attachment_type.TEXT)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)


@allure.epic("商城后台系统")
@allure.feature("用户模块")
@allure.story("充值接口")
@allure.title("全字段正常金额为10万")
def test_cz2():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/acc/recharge'

    req = {
  "accountName": "yyjj012",
  "changeMoney": 10000000

}


    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    allure.attach("预期结果:{},实际结果:{}".format(200, resp.status_code), "响应状态码断言", allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code, 200)
    allure.attach("预期结果:{},实际结果:{}".format(2000,body['code']),"响应code",allure.attachment_type.TEXT)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)






