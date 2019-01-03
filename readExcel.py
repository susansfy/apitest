
#coding:utf-8

import xlrd

class ReadExcel():

	def  __init__(self,fileName,SheetName="Sheet1"):
		self.data = xlrd.open_workbook(fileName)
		self.table = self.data.sheet_by_name(SheetName)

		#获取总行数、列数
		self.nrows = self.table.nrows
		self.ncols = self.table.ncols

	def readExcel(self):

		
		if self.nrows>1:
			self.keys = self.table.row_values(0)

			listApiData = []

			for col in range(1,self.nrows):
				values = self.table.row_values(col)
				api_dict = dict(zip(self.keys,values))
				listApiData.append(api_dict)

			return listApiData
		else:
			print(u"表格未填写数据")
			return None

# if __name__ == '__main__':
# 	filename = "D:\\learn\\Python\\codetest\\ddttest\\ddttest1.xlsx"
# 	sheetname = "Sheet1"
# 	s = ReadExcel(filename,sheetname).readExcel()
# 	print (s)
# 	print type(s)

###
###[{u'body': u'', u'type': u'json', u'id': 2.0}]
###<type 'list'>
#结果为列表，列表内是字典，一行数据一个字典



