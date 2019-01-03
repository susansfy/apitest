#coding:utf-8

import unittest
from ddt import ddt,data,file_data,unpack


@ddt
class FooTest(unittest.TestCase):
    
    @file_data('test_dict.json')
    def test_file_data_json_dict(self,start,end,value):
        print "this is start"
        print start
        print "this is end"
        print end
        print "this is value"
        print value
        print "this is json_dict"
        
        '''
        .this is start
        -1.0
        this is end
        0.0
        this is value
        -0.5
        this is json_dict
        this is start
        -2
        this is end
        0
        this is value
        -1
        this is json_dict
        this is start
        0.0
        this is end
        1.0
        this is value
        0.5
        this is json_dict
        this is start
        0
        this is end
        2
        this is value
        1
        this is json_dict
        '''
        
    @file_data('test_data_dict.json')
    def atest_file_data_dict_json(self,value):
        print value
        
        '''
        .[10, 12, 15]
        [15, 12, 50]
        '''
        
    
if __name__ == '__main__':
    unittest.main()