#! /user/bin/ env python3
# -*- coding: utf-8 -*-
# Author:GaoWei Tang
import os, sys
import unittest
import requests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class saveCustomerPhone(unittest.TestCase):
    '''掌上生活登录接口'''

    def setUp(self):
        self.base_host = 'http://test14.bbf.t.xianghuanji.com'
        self.base_path = '/api/v2/userOauth/saveCustomerPhone'
        self.base_url = self.base_host + self.base_path

    def tearDown(self):
        print(self.result)

    def atLast(self):
        self.assertEqual(self.result['status'], 104)
        self.assertEqual(self.result['msg'], '参数错误')
        self.assertEqual(self.result['message'], '参数错误')

    def test_all_null(self):
        '''所有参数为空'''
        playload = {'oauth_id': None,'type':None,'phone':None}
        r = requests.post(self.base_url,data=playload)
        self.result = r.json()
        self.atLast()

    def test_all_is_null(self):
        '''所有参数为null'''
        playload = {'oauth_id': 'null', 'type': 'null', 'phone': ''}
        r = requests.post(self.base_url, data=playload)
        self.result = r.json()
        self.atLast()

    def test__phone_exist(self):
        '''phone已经存在'''
        playload = {'oauth_id': 'asd123456', 'type': '4', 'phone': '13012830533'}
        r = requests.post(self.base_url, data=playload)
        self.result = r.json()
        self.atLast()

    def test_oauth_id_exist(self):
        '''oauth_id已经存在'''
        playload = {'oauth_id': 'asd123456', 'type': '4', 'phone': '13012830532'}
        r = requests.post(self.base_url, data=playload)
        self.result = r.json()
        self.atLast()

    def test_phone_type_error(self):
        '''phone格式错误'''
        playload = {'oauth_id': 'asd1234561', 'type': '4', 'phone': '4'}
        r = requests.post(self.base_url,data=playload)
        self.result = r.json()
        self.atLast()

    def test_success(self):
        '''账号注册成功'''
        payload = {'oauth_id': 'asddsa3', 'type': '4', 'phone': '15010000105'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 101)
        self.assertEqual(self.result['data']['is_bind'], True)
        self.assertEqual(self.result['data']['type'], '4')


if __name__ == '__main__':
    unittest.main()


