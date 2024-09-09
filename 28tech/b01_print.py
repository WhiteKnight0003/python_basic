# print - dùng để in nội dung . có thể là xâu ký tự - lên màn hình
  
'''
cú pháp : print(object , sep = seperator, end = end)
object : các đối tượng
sep : phân các giữa các đối tượng khi in , nếu k có tham số này mặc định sẽ là dấu cách
end : chỉ ra kí tự đc in ở cuối dòng , nếu k có tham số này mặc định sẽ là xuống dòng

'''

a = 100
b = 200
c = 300
print(a, b, c) 
print('tienchung')

# nếu chạy thế này nó sẽ cho dòng sau xuống dòng như chú thích trên
# 100 200 300
# tienchung

print('le','tiến', 'chung', sep = "$--")  #  le$--tiến$--chung
print('le','tiến', 'chung', sep = "$--", end = "----------------")  #   le$--tiến$--chung----------------