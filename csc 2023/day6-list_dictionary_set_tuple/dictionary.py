'''
- giống như map 
- là 1 data struct thuộc nhóm sequence
- gồm nhiều phần tử , mỗi phần tử gồm key:value
- key duy nhất b, value có thể trùng
- kiểu data của key có thể là string , number  or tuple ...
- value có thể là numbers, string , tuple, list, dictionảy , ...
'''

# khởi tạo
'''
+ dictionary_name = {key1: value1 , key2:value2, .....}
+ khởi tạo rỗng 
    + dic_1 = {}
    + dic_2 = dict()
'''

#truy xuất value
# dic[key]  - nếu k có key -> keyError
# nếu value có chứa các dictionary con ta dùng dic[key][key]... để try cập dần vào các dictionary con
# dic.get(key) - nếu k có key trả về None chứ không có bug


# thêm mới  / cập nhật 
'''
+ nếu key chưa xuất hiện : dict[key] = value  -> thêm mới 
+ nếu key đã xuất hiện : dict[key] = new value -> cập nhật

'''

#func & methods
'''
+ len(dict) - số phần tử 

+ xóa 
    + xóa theo key : del(dict[key])
    + xóa tất cả phần tử : dict.clear()
    + xóa luôn cả dict : del(dct)
'''

# chuyển thành dạng chuỗi
'''
dict = {...}
s = str(dict)
'''

# tạo bản sao
# dict1 = dict.copy()   - nếu muốn tách vùng nhớ ra thì dùng copy() - không thì gán bthg


# tạo dictionary with danh sách key từ sequence
'''
list 1 = [1,2,3,4]
dict1 = dict.fromkeys(list1) -> nó sẽ trả về {1:None , 2: None, 3:None , 4:None}

list2 = [2,3,4,5]
dict2 = dict.fromkeys(list2,'res') -> {2:'res' , 3:'res', 4:'res', 5:'res'}
'''

# truy xuất danh sách 
'''

dict1 = { 1:3,2:5,3:1,4:8,6:9 }
# trả về danh sách cách key
dict_key = dict1.keys()           #dict_keys([1, 2, 3, 4, 6])
list_key = list(dict1.keys())    #[1, 2, 3, 4, 6]

# trả về danh sách value
dict_val = dict1.values()           #dict_values([3, 5, 1, 8, 9])
list_val = list(dict1.values())    #[3, 5, 1, 8, 9]
print()
'''

# update giá trị 
'''
dict1 = {1:3, 2:4, 5:7}
dict2 = {6:0,9:3}
dict1.update(dict2) #{1: 3, 2: 4, 5: 7, 6: 0, 9: 3}
print()
'''


# for 
'''
dict1={}
# lấy cả key + value
for key,value in dict1.items():
    print(f'{key}-{value}')

# chỉ lấy key
for item in dict1.keys():
    print(item)

# chỉ lấy value
for item in dict1.values():
    print(item)

'''


#zip : duyệt nhiều dictionary cùng lúc 
''' - trùng khóa thì nó sẽ thay thế value mới vào key đó
listMaSo = ['01', '02', '03', '04']
listDonGia = [100,200,300,400]
dictDSHH = {}

for ms,dg in zip(listMaSo,listDonGia):
    dictDSHH[ms] = dg
'''

#dict_comprehension - cách duyệt nhanh hơn
listMaSo = ['01', '02', '03', '04']
listDonGia = [100,200,300,400]

# 1 : no if
dictHH = {ms:dg for  ms,dg in zip(listMaSo,listDonGia)} 
print(dictHH) #{'01': 100, '02': 200, '03': 300, '04': 400}

#2
dictHH = {ms:dg for  ms,dg in zip(listMaSo,listDonGia) if dg>200}  #{'03': 300, '04': 400}
print(dictHH) #{'01': 100, '02': 200, '03': 300, '04': 400}