#coding:utf-8
from readExcel import ReadExcel
import requests
import json

class  SendRequest():
	"""docstring for  SendRequest"""
	def sendRequests(self,s,apiData):
		try:
			method = apiData["method"]

			url = apiData["url"]
			if apiData["params"] == "":
				par = None
			else:
				par = eval(apiData["params"])

			if apiData["headers"] == "":
				h = None
			else:
				h = apiData["headers"]

			if apiData["body"] == "":
				body_data = None
			else:
				body_data = eval(apiData["body"])

			apitype = apiData["type"]
			v = False
			if apitype == "json":
				body = json.dumps(body_data)
			if apitype == "data":
				body = body_data
			else:
				body = body_data

			#发送请求
			re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
			#req = json.dumps(re,encoding="UTF-8",ensure_ascii=False)
			# print(body)
			# print type(re)
			resp = re.json()
			#print resp
			res = json.dumps(resp,encoding="utf-8",ensure_ascii=False,indent=4)
			#print type(res)  ---类型是unicode
			return res

		except Exception as e:
			print(e)
		
# if __name__ == '__main__':
# 	s = requests.session()
# 	filename = "D:\\learn\\Python\\codetest\\ddttest\\ddttest1.xlsx"
# 	sheetname = "Sheet1"
# 	testdata = ReadExcel(filename,sheetname).readExcel()
# 	#testdata = ReadExcel.readExcel()
# 	response = SendRequest().sendRequests(s,testdata[1])
#  
# 	# listres =  list(response)
# 	# print (json.dumps(listres,encoding="utf-8",ensure_ascii=False,indent=4))
# 	# print (response.json())
#  
# 	resp = response.json()
# 	print (json.dumps(resp,encoding="utf-8",ensure_ascii=False,indent=4))
# 
# 	
	