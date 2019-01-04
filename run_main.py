#! /usr/bin/env python ???
#coding:utf-8
'''
Created on 2019年1月4日

@author: susan
'''

import unittest
import time
import os
from casetest2 import Test1
import HTMLTestRunner

report_path = "D:\\learn\\Python\\codetest\\ddttest\\report\\"

if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(Test1('test_api'))
#     
    #discover = unittest.defaultTestLoader.discover('e:\\workspace\\GXback2\\test_case', pattern='*test.py')
    now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    filename = report_path+now+'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='REPORT',description='RESULT')
    discover = unittest.defaultTestLoader.discover("./",pattern="run_main.py",top_level_dir=None)
    runner.run(discover)
    fp.close()