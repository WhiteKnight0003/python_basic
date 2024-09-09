'''
- vẫn là set và có sắp xếp theo thứ tự
- 1 cấu trúc thuộc nhóm sequence
- mỗi phần tử trong set là duy nhất, không trùng nhau và giá trị của các phần tử là không đổi
- các phần tử set không theo thứ tự thêm vào , không dùng index
'''

# khởi tạo
# name_set = {value1, value2 , value3 , ....}

# 1 số phép toán
'''
# union -> (A V B) -> phép hợp
setA = {1,2,3,6,7}
setB = {1,4,5,8,9}
setC = setA | setB 
print(setC) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#interSection
# lấy các phần tử (A ^ B)  -> giao
setD = setA & setB
print(setD)  #{1}

#Difference
#lấy các phần tử chỉ xuất hiện trong A mà không xuất hiện trong B
setF = setA - setB
print(setF) #{2, 3, 6, 7}

# Symmetric Difference - trả về các phần tử không cùng xuất hiện trong các set
# (A V B ) - (A ^ B)
setG = setA ^ setB #{2, 3, 4, 5, 6, 7, 8, 9}
print(setG)
'''

# các hàm len , max, min, sum vẫn vậy 

# sắp xếp tăng , giảm dần
'''
# cú pháp :
    + tăng : sorted(set_name)
    + giảm : sorted(set_name, reverse = True)
'''

# chuyển set -> list
set_name = {1,2,3,4}
list_name = list(set_name)
# chuyển list -> set -> nó sẽ tự loại bỏ các phần tử trùng lặp
setA = set(list_name)

#chuyển set -> tuple
tuple_A = tuple(set_name) 
# chuyển tuple -> set -> -> nó sẽ tự loại bỏ các phần tử trùng lặp
set_B = set(tuple_A)

# khi chuyển đôi, nếu đã ra kết quả thì bạn nên del() những cáu thừa ra khỏi bộ nhớ