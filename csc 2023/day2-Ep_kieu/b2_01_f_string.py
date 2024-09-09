
tienLuong = 50000000
hoTen = 'Lê Tiến Chung'
hsl = 2.4434


strTT1 = f' Họ tên :{hoTen}\n Tiển lương : {tienLuong:,}VND\n Hệ số lương: {hsl:.2f}\n' # trong ngoặc nhọn là tên biến
# hsl:.2f : làm tròn đến 2 chữ số thập phân
# tienluong:,  - làm cho tiền có , giữa các mệnh giá
print('-'*50)
print(strTT1)
print('-'*50) # sopy nó 50 lần
'''
 Họ tên :Lê Tiến Chung
 Tiển lương : 50,000,000VND
 Hệ số lương: 2.44

 '''


strTT2 = f' Họ tên :{hoTen}\n Tiển lương : {tienLuong:,.2f}VND\n Hệ số lương: {hsl:.2f}\n' # trong ngoặc nhọn là tên biến
# hsl:.2f : làm tròn đến 2 chữ số thập phân
# tienluong:,.2f  - có phân cách giữa ngàn  và có 2 chữ số 0 sau dấu . thập phân
print('-'*50)
print(strTT2)
print('-'*50) # sopy nó 50 lần