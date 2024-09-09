'''
- func là tập hợp các dòng code được viết để thực hiện 1 chức năng nào đó
- mục đích xây dựng func nhằm tái sử dụng khi cần
- func cung cấp module tốt hơn cho ứng dụng và mức độ tái sử dụng code cao hơn
- python cung cấp rất nhiều func có sẵn (built-in function)- và ng dùng cũng có thể tự xây dựng (user-defined function)
'''

# các biến toàn cục luôn tồn tại xuyên xuất chương trình
# các biến cục bộ chỉ tồn tại khi các hàm chạy và nó sẽ kết thúc khi hàm thực hiện xong
# xây dựng function
'''
def function_name(parameters):
    # mô tả function
    các dòng lệnh
    return [expression] nếu có


vd :
def tinhtong(a,b,c=1): # gán c=1
    return a+b+c

def tinh_tich_day_so(*day_so): # *day_so : truyền vào 1 dãy số
    # giống như bạn dùng max , bạn có thể truyền vào rất là nhiều số
    kq=1
    for i in day_so:
        kq*=i
    return kq

if __name__ == '__main__':
    print(tinhtong(3,4)) # 8  -> a =3, b=4, c=1
    print(tinhtong(3,8,9)) # 20 -> a=3,b=8,c=9
    print(tinh_tich_day_so(1,2,3,4,5))

    listN =[4,3,6] 
    print(tinh_tich_day_so(*listN)) # truyền 1 list, set, tuple đều được cả  nhưng phải có * ở đầu tiên
'''


# anonumous Function (lambda)
'''
- phương thức ẩn danh : nó không được công khai = cách sử dụng def mà được viết ngắn gọn bằng cách sử dụng lambda để tạo ra các phương thức ngắn với 1 dòng lệnh 
# khởi tạo
lambda [parameter1[, parameter2...]]:
expression

# chú ý
- lambda có thể có 1 or nhiều parameter nhưng chỉ trả về 1 value duy nhất
- lambda không thể chứa quá nhiều command or expression - lệnh or biểu thức
-lambda không thể được gọi trực tiếp để in kết quả bởi nó yêu cầu 1 expression
- lamdba  có local namespace của nó  và k thể truy cập các biến khác và biến bên trong phạm vi global namespace
'''

import math
# define 
s = lambda x,n : math.pow(math.pow(x,2)+1,n)
s1 = lambda x:x*x
s2 = lambda x: x%2==0
print(s(2,3)) #125.0
print(s1(3)) #9
print(s2(3)) #False


9
False