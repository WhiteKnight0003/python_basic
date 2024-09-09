n = int(input("Nhập vào n"))
a,b=0,1
strKQ = f'{a},'
for i in range(n):
    a,b= b, a+b
    strKQ+=f'{a},'
print(strKQ)