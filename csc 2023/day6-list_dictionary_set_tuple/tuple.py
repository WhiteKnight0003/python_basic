'''
- là cấu trúc thuộc nhóm sequence
- giới hạn , cố định số phần tử và không thay đổi giá trị phần tử
- gồm nhiều phần tử và có thể truy cập theo vị trí
- cũng có thể chứ nhiều kiểu dữ liệu 
'''

#tạo tuple
'''
+ name_tuple = (pt1, pt2, ....) - có thể không dùng () khi tạo tuple
+ vd
  +) tupe1 = (1,2,3,....)
  +) nếu k có dấu phẩy đằng sau thì nó sẽ là int chứ k phải tupe
      ++) type2 = 1,   - type   -> type2(1,)
      ++) type2 = 1    - int    -> type2(1)

'''

# truy xuất
'''
+ tuple1[index] - truy cập vào phâng tử vị trí index
+ tuple2[start:end] - lấy phần tử từ vị trí start -> end-1
'''

# tuple không thể thay đổi , do đó ta không thể cập nhật / xóa phần tử trong tuple
# chỉ có thể xóa đc cả tuple
# del(tuple_name)


# các hàm cơ bản vẫn giống list
# nhưng không có sort, reverse , remove , pop, extend , append - các phương thức thay đổi phần tử

#copy các phần tử của list sang tuple
'''
list_name = [1,2,3,4,5,6]
tup = tuple(list_name)
'''