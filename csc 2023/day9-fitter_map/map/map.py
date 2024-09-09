import math
listA = [4,3,5,2]
listB = [7,3,4]

listA2 = list(map(lambda x: x**2,listA))
listB2 = list(map(lambda x:math.isqrt(x), listB))
print(listA2) #[16, 9, 25, 4]
print(listB2) #[2, 1, 2]

sumAB = list(map(lambda x,y:x+y,listA,listB))
print(sumAB) #[11, 6, 9]

# chỉ lấy họ tên
listDSHS = [
    ['001','Lê Văn A', 9.5],
    ['002','Lê Văn B', 3.5],
    ['003','Lê Văn C', 4.5],
    ['004','Lê Văn D', 6.5],
    ['005','Lê Văn E', 7.5],
    ['006','Lê Văn F', 2]
]

listHT = list(map(lambda item:item[1], listDSHS))
print(listHT)