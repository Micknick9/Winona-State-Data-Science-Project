import xlrd
wb = xlrd.open_workbook("C:/Users/kolto/Google Drive/CA_Ex.xlsx")
sh1 = wb.sheet_by_index(0)
for index in range(4, 5):
    a = int(input("Starting Row?"))-1
    b = int(input("Ending Row?"))-1
    data = sh1.col_values(index, start_rowx=a, end_rowx=b)
su = sum(data)
div = b - a
avg = su / div
print (avg)
