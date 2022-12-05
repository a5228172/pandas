import pypyodbc,openpyxl
import pandas as pd,re,time,os
import win32com.client
from win32com.client import Dispatch
def muban():
	app = Dispatch("Excel.Application")
	app.Visible = 1
	app.ScreenUpdating =True
	#xlbook.Sheets.Count工作表数量
	#AskToUpdateLinks如果 Microsoft Excel 打开带有链接的文件时询问用户是否更新链接，则该值为 True。 如果 Microsoft Excel 自动更新链接并且不显示对话框，则该值为 False。 读/写 Boolean
	# app.ScreenUpdating = False 		#屏幕不显示EXCEL
	assert()
	try:
		xlbook=app.Workbooks.Open(r'C:\Users\Administrator\Desktop\123.xls')  # xlsm也可以
	except:
		pass
	a1 = [x.name for x in xlbook.Sheets]#所有工作表名称
	c1 = xlbook.Sheets(1)
	print(xlbook.Sheets(1).UsedRange.Columns.Count)
	print(xlbook.Sheets(1).UsedRange.Rows.Count)
	print(c1.Cells(2,1).Value)
	c1.Cells(2,1).value =123456
	# xlbook.Sheets(1).Activate.Range("i:i").EntireColumn.AutoFit
	# xlbook.Sheets(1).Columns(G).AutoFit
	c1.Columns("B:X").EntireColumn.AutoFit
	c1.AutoFilterMode = True
	# c1.Selection.AutoFi
	# xlbook.Close(SaveChanges=True)
	# app.ScreenUpdating = True
	# app.Quit()
	# app.AskToUpdateLinks = True
	# app.Run("Macro1")  # 宏的名字
	# xlbook.Close(SaveChanges=True)
	# app.Quit()
	# c1.Cells(x+1,i+1).Font.ColorIndex = 3
	# c1.Cells(x+1,i+1).Interior.ColorIndex = 4 #单元格颜色
	
def duibi3():
	app = Dispatch("Excel.Application")
	app.Visible = 1	
	ss = r'E:\er\py\v20查数据\V20产品库\V20查询表.xlsx'
	try:
		xlbook=app.Workbooks(ss)
	except:
		xlbook=app.Workbooks.Open(ss)
	a1 = [x.name for x in xlbook.Sheets]
	# print(a1)
	c1 = xlbook.Sheets('核对')
	c2 = xlbook.Sheets('核对校验')
	c1.Activate()
	for i in range(0,c1.UsedRange.Columns.Count):
		# for x in range(1,2):	
		for x in range(0,c1.UsedRange.Rows.Count):
	
			print(c2.Cells(x+1,i+1).value)
			if c1.Cells(x+1,i+1).value=='None' or c1.Cells(x+1,i+1).value == '' :
				c1.Cells(x+1,i+1).value =''
			if c2.Cells(x+1,i+1).value=='None' or c2.Cells(x+1,i+1).value == '' :
				c2.Cells(x+1,i+1).value =''

			if c1.Cells(x+1,i+1).value !=c2.Cells(x+1,i+1).value:
				# c1.Cells(x+1,i+1).Font.ColorIndex = 3
				c1.Cells(x+1,i+1).Interior.ColorIndex = 4
			else:
				c1.Cells(x+1,i+1).Interior.ColorIndex = 0
	# c1.Cells(2,1).value =123456
	print(c1)
def main3():
	app =Dispatch("Excel.Application")
	ss= r'E:\er\门板123.xlsx'
	xlbook=app.Workbooks(ss)
	xlbook.Activate()
	c1 = xlbook.Sheets(1)
	hangshu = c1.UsedRange.Rows.Count
	c1.Rows(f'{hangshu}:{hangshu}').Copy()
	for x in range(3):
		hangshu = hangshu+1
		c1.Rows(f'{hangshu}:{hangshu}').Select()
		c1.Paste()
	print(hangshu)
	
if __name__ == '__main__':
	# qushuju()
	duibi3()
	
