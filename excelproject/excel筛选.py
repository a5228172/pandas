#coding:utf-8
import os
from win32com.client import Dispatch
from shutil import copyfile
import pandas as pd,re,time,os,pyperclip
def shuaixuan(st = r'E:\er\预览图更换\门板\K定制门板.xlsx'):
	st = pd.read_excel(st).fillna('')
	a3 = pyperclip.paste().split("\n")
	for x in a3[:]:
		if '' == x:
			a3.remove(x)
	for x in range(0,len(a3)):
		if '\r' in a3[x]:
			a3[x] = a3[x].replace('\r','')
	st1 = st.iloc[0:2,:]
	print(st1)
	for x in a3:
		st2 = st.loc[st.door_shape.apply(lambda a : x ==a)]
		st1 = st1.append(st2)
	st1.iloc[2:,:].to_excel(r'筛选EXCEL.xlsx',index = False)
	print(st1)