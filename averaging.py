#---Imports---
import xlrd

#---Defs---
def average(path):
    wb=xlrd.open_workbook(path)
    sh1=wb.sheet_by_index(0)
    for index in range(4, 5):
        a=int(input("Starting Row?"))-1
        b=int(input("Ending Row?"))-1
    data=sh1.col_values(index, start_rowx=a, end_rowx=b)
    su=sum(data)
    div=b-a
    avg=su/div
    print (avg)

def weightAge(path, avg):
    wb=xlrd.open_workbook(path)
    sh1=wb.sheet_by_index(0)
    

#---Actuall Program---
path=input("What is the path of your data relative to this program?")
avg=average(path)
weightAge(path, avg)
