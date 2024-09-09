from calendar import *

namNhuan = isleap(2000) # check năm nhuận

Ngay = monthrange(2024,4) #(0,30)  - 0 là monday - ngày đầu tiên của tháng bắt đầu vào thứ 2 , 30 là số ngày trong tháng
print(Ngay, Ngay[0], Ngay[1]) #(0, 30) 0 30

lichThang = monthcalendar(2024,7)
print(lichThang) # nó chứa các list - hay các tuần , mỗi tuần chứa ngày số bn của tháng - t2 đàu tiên chủ nhật cuối cùng
# print()