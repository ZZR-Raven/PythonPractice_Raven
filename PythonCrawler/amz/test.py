import xlrd 

workbook=xlrd.open_workbook('amzuser.xlsx')
# print (workbook.sheet_names())
userinfo = workbook.sheet_by_name('Sheet1')
cell_value = userinfo.cell(1, 1).value
print(cell_value)
# cell_A = userinfo.cell(1,1).value print(cell_A) 