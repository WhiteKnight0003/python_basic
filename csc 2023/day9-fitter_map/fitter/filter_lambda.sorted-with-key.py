# Dùng để lọc các item trong sequence , tạo ra 1 sqquence mới với các item thỏa điều kiện của function

# cú pháp
# filter(function, sequence) 

listN = [5,6,7,3,5,12,44,8,10,9]
# lọc danh sách số chẵn , loaij bor trung lap
listEven = set(filter(lambda x: x%2==0, listN))
print(listEven)

# tính tổng các số là bội của 3
res = sum(list(filter(lambda x: x%3==0,listN)))
print(res)

# lấy ng có họ lê
listName = [
    "Lê văn A",
    "Trần thị B",
    "Lê đình C",
    "Lý Quốc D"
]
listRes = list(filter(lambda x:x[0:3].lower()=='lê ', listName))
print(listRes)


# duyệt hs đậu
listDSHS = [
    ['001','Lê Văn A', 9.5],
    ['002','Lê Văn B', 3.5],
    ['003','Lê Văn C', 4.5],
    ['004','Lê Văn D', 6.5],
    ['005','Lê Văn E', 7.5],
    ['006','Lê Văn F', 2]
]


#sắp xếp listDSHS tăng dần theo điểm
# listDSHS.sort(key=lambda item:item[2]) # sort dựa trên điểm số tăng
listDSHS.sort(key=lambda item:item[2], reverse= True) # sort giảm theo điểm
listDau = list(filter(lambda item:item[2]>=5,listDSHS))
print(listDau)