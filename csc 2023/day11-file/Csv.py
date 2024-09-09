#csv file - như excel
# import csv khi làm việc với loại này

#mở đọc file csv
'''
- Cú pháp mở : f= open(filename)
- Cú pháp đọc : csv.reader(f)
- cú pháp đóng : f.close()
'''

# mở - đọc nội dung từng dòng - đưa vào list- đóng 
# nếu ở kết quả có tiền tố \ufeff -> phải dùng đến  encoding='utf-8-sig'

# import csv
# data = []
# with open('E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\DuLieu-csv\DuLieu\dsnv.csv', 'r',encoding='utf-8-sig') as f:
#     for row in csv.reader(f):
#         data.append(row)
#     f.close()

# print()
# print(data)
    
# ghi 1 dòng - mỗi componet vào 1 ô - writerow - không có s 
# import csv
# with open('E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\DuLieu-csv\DuLieu\dssv1.csv', 'w',encoding='utf-8-sig', newline='') as f:
#     listThongTin1 = ['MS01','Trần','An','42347326']
#     csv.writer(f).writerow(listThongTin1)
# print('ghi thành công1')

# tạo tệp tin mới để ghi - ghi nhiều dòng  - mỗi componet vào 1 ô  - writerows - có s
import csv
with open('E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\DuLieu-csv\DuLieu\dssv2.csv', 'w',encoding='utf-8-sig', newline='') as f:
    listThongTin2 =[
        ['MS01','Trần','An','42347326'],
        ['MS02','Trầnd','Ang','423347326'],
        ['MS03','Trầnf','Anf','423447326'],
        ['MS04','Trầndsd','Ans','423647326']
    ] 
    csv.writer(f).writerows(listThongTin2)
print('ghi thành công2')


# dùng tệp đã tồn tại để ghi thêm
# import csv
# with open('E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\DuLieu-csv\DuLieu\dssv1.csv', 'a',encoding='utf-8-sig', newline='') as f:
#     listThongTin3 = ['MSư0a','Trầgn','Anf','255299326']
#     csv.writer(f).writerow(listThongTin3)
# print('ghi thành công1')