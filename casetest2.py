#coding:utf-8
'''
Created on 2018年12月27日

@author: susan
'''

import unittest
import requests
from ddt import ddt,data,unpack
import os
from readExcel import ReadExcel
from sendRequest import SendRequest

filename = "D:\\learn\\Python\\codetest\\ddttest\\ddttest1.xlsx"
sheetname = "Sheet1"
testdata = ReadExcel(filename,sheetname).readExcel()

@ddt
class Test1(unittest.TestCase):
    
    def setUp(self):
        self.s = requests.sessions()
        
    def tearDown(self):
        pass
    
    @data(*testdata)
    def test_api(self,data):
        re = SendRequest().sendRequests(self.s,testdata[1])
        
        