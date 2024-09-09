# cú pháp : input(prompt)
# input() - trả về str nên phải chú ý ép kiểu

# nhập 1 số
# n = int(input("Nhap n : "))
# print(n)


# nhập nhiều số
'''
- nhập cả dòng = input
- dùng split để tách số các trong xâu input ra
- dùng map để ép các xâu đc tách trong input sang int hay float tùy ý
'''

a , b, c, d = map(int, input().split())
print(a,b,c,d)
'''nó sẽ như thế này
b1 : nhập
   s = input('Nhap 4 so : ')
b2 : cắt ra thành 1 list
   a = s.split()
b3 : dùng map để ánh xạ và ép các phần tử theo kiểu int
   x,y,z,t = map(int ,a)
'''