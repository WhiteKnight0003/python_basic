from time import * # khai báo thư viện time

print(time()) # trả về time hiện tại của hê thống dạng số
#1720949192.7553864

print(localtime(time()))
#time.struct_time(tm_year=2024, tm_mon=7, tm_mday=14, tm_hour=16, tm_min=26, tm_sec=32, tm_wday=6, tm_yday=196, tm_isdst=0)

print(asctime(localtime(time())))
#Sun Jul 14 16:27:21 2024
