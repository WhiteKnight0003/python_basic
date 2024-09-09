'''
list1 = [1,5,3,4,22,3]
list2 = list1 # list 2 tham chiếu đến vùng nhớ mà list 1 quản lý nên khi list2 thay đổi sẽ thay đổi cả list1
list3 = list1.copy() #copy
list2[3]=10 # gán lại
print(list1, list2, list3) #[1, 5, 3, 10, 22, 3]   [1, 5, 3, 10, 22, 3]    [1, 5, 3, 4, 22, 3]

#list1 và list2 sẽ có id giống nhau còn list3 sẽ khác 2 cái kia
'''
# đọc thứ :
from datetime import *
try:
    strNgay=input("Nhập vào ngày (dd/mm/yyyy): ")
    ngay = datetime.strptime(strNgay,'%d/%m/%Y')
except ValueError:
    print('>>> Lỗi : Ngày nhập vào không hợp lệ')
else:
    list_Thu = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']
    index_Ngay = ngay.weekday()
    thuTiengViet = list_Thu[index_Ngay]
    thuTiengAnh = ngay.strftime('%A')

    print('Thứ tiếng việt : ',thuTiengViet)
    print('Thứ tiếng Anh : ',thuTiengAnh)
