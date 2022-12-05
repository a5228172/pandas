# coding: utf-8
import pyperclip
import json,os,sys
import pandas as pd
import zichuan
def main():
	# os.chdir(os.path.abspath(os.path.dirname(__file__)))

	ss = r'123.xlsx'
	zichuan.excelguanbi(ss)
	os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
	a3 =pyperclip.paste()
	a3 = json.loads(a3)
	print(a3)
	# a3 = a3['data']['data']
	try:
		a3 = a3['data']['items']
	except:
		a3 = a3['data']
	pd.DataFrame(a3).to_excel(ss,index=False)
	zichuan.exceldakai(ss)
if __name__ == '__main__':

	
	
	main()
	


