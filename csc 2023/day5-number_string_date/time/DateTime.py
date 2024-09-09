
'''


from datetime import *

print(datetime.now())  #datetime.today()  - lấy đc toàn bộ day, month, year, hour ,...
#2024-07-14 16:29:09.477156
hour = datetime.now().hour
print(datetime.now().year)

print(date.today())  # chỉ lấy đc day, month , year
#2024-07-14 
ngay = date.today().day
thang = date.today().month
nam = date.today().year
print(ngay, thang, nam)

print(repr(date.today())) # chuyển đối tượng này thành str
print(eval('repr(date.today())')) # chuyển đối tượng này về ban đầu
'''


from datetime import *
'''
# khởi tạo ngày theo địn dạng
# strptime(str muốn chuyển đổi - phải có định dạng y như bên định dạng , định dạng)
NgayHD = datetime.strptime('25/3/2024','%d/%m/%Y')
NgayKH = datetime.strptime('25-3-2024','%d-%m-%Y') #y - năm gồm 2 chữ số cuối , #Y - năm đầy đủ 4 số

#chuyển từ biểu thức ngày -> chuỗi thỏa theo mẫu định dạng
NgaySinh = date(2021,3,4)
NgaySinh2 = date(2022,6,21)
strNs = NgaySinh.strftime('%a %d/%y/%Y') #'Thu 04/21/2021' - %a : viết tắt thứ chỉ 3 kí tự
strNs2 = NgaySinh.strftime('%A %d/%y/%Y') #'Thursday 04/21/2021' - %A : viết đầy đủ thứ  - có thể đổi chỗ chúng

#  Monday- 0 , ..., Sunday - 6
iThu = NgaySinh.weekday() # trả về chỉ số trong tuần
print()


#timedelta - kq khi trừ 2 ngày cho nhau
d1 = datetime(2023,6,7,7,30,00)
d2 = datetime(2024,8,3,6,00,35)
t1 = d2-d1 #datetime.timedelta(days=422, seconds=81035) dạng của t1 
#422 days, 22:30:35
print(t1)

NgayMai = date.today() + timedelta(days=1) # ->date
NgayHomQua1 = date.today() + timedelta(days=-1)
NgayHomQua2 = date.today() - timedelta(days=1)

t = timedelta(days=5, hours=4,minutes=20,seconds=7)
tong_So_giay = t.total_seconds()
print()

'''