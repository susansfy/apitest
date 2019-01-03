#coding:utf-8
'''
Created on 2018年12月27日

@author: susan
'''

import unittest
import requests
from ddt import ddt,data,unpack
import os
import json
from readExcel import ReadExcel
from sendRequest import SendRequest
import string

filename = "D:\\learn\\Python\\codetest\\ddttest\\ddttest1.xlsx"
sheetname = "Sheet1"
testdata = ReadExcel(filename,sheetname).readExcel()

@ddt
class Test1(unittest.TestCase):
    
    def setUp(self):
        self.s = requests.Session()
        
    def tearDown(self):
        pass
    
    @data(*testdata)
    def test_api(self,data):
        re = SendRequest().sendRequests(self.s,data)
    
        res = json.loads(re)
        
        #print res  
        #print type(res)  ---类型是字典
        #print res['data']['introduction']
        #self.assertEqual(u"有效", res['data']['statusTip'], u'状态有误%s'%res['data']['statusTip'])
        #print "success"
        #print data["exceptvalue"] --excel文件中的exceptvalue值
        except_value = data['exceptvalue']
        
        result = re.find(except_value)
        self.assertEqual(True, result>=0, u"不相等")
        
        
        
if __name__ =='__main__':
    unittest.main()
        