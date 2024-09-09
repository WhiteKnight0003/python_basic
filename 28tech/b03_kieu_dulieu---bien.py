'''  biến sẽ được tạo và xác định kiểu dữ liệu tự động (dynamic typing) khi bạn gán giá trị cho nó
     để biết kiểu dữ liệu của biến - dùng hàm type(biến)

a = 100
b = "sdasdsa"
print(type(a)) -> <class 'int'>
print(type(b)) -> <class 'str'>

# Tuple
# Kiểu dữ liệu Tuple trong python là một collection có thứ tự, không thể thay đổi. Cho phép chứa dữ liệu trùng lặp.


#  trong tên biến k có dấu cách, k được bắt đầu bằng chữ số , k các ký tự các biệt , tên biến phân biệt hoa thường
'''


# kiểu dữ liệu
'''có 3 loại dũ liệu số 
số nguyên - integer
số thực dấu phẩy động - floating - point numbers
số phức - complex numbers 

a = 100
b = 3.543
c = 5 + 3j
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
'''


###
'''Số nguyên - integer
- nó không bị giới hạn về chữ số (kể cả với số nguyên lớn)
- bạn có thể in ra các số nguyên theo hệ 10 từ các hệ số 2 , 8 , 16
a = 0b1101 (0b hoặc 0B đại diện cho hệ nhị phân - Binary)
b = 0o123  (0o hoặc 0O đại diện cho hệ bát phân - Octal)
c = 0x22A  (0x hoặc 0X đại diện cho hệ thập lục phân - hexadecimal) 
print(a,b,c) 13 83 554
'''


###
''' số thực - floating
- là số nguyên kèm phần thập phân 
- có thể lưu số lớn nhất xấp xỉ 1.8*10^318 , số lớn hơn nó được mô tả bởi   inf (Infinity)
- Giá trị số thực nhỏ nhất có thể lưu là 5.0*10^-324 , số nhỏ hơn nó đc cai như là 0

a = 3.5
b = 3e5
c = 1.9e308
d = 5.4e-325 
print(a,b,c,d) -> 3.5 300000.0 inf 0.0

- in ra số dấu phẩy thập phân
a = 28.543543534
print('%.2f' % a)
print(round(a,2))
print('{:.2f}'.format(a))
'''

###
''' số phức - Complex
- gồm 2 phần thực (real part) và phần ảo (imaginary part) + j    (3 + 5j)
- cách lấy phần thực và phần ảo của số phức x    : x.real  -- x.imag

a = 3+5j  
print(a.real, a.imag)   ->  3.0 5.0
'''


### 
''' kiểu dữ liệu đúng sai - bool
- chỉ lưu 2 giá trị true or false
- các giá trị true : các xâu khác rỗng, con số khác 0

print(bool(100))   -> True
print(bool(0))     ->    False
print(bool("sadasdas"))    -> True
print(bool("")) -> False

'''


###
''' xâu ký tự - string 
- 1 ký tự cũng là xâu ký tự 
- nằm giữa dấu nháy kép or nháy đơn
- cắt 1 chuỗi
  str = 'hellooo'
  print(str[2:5]) - cắt ksi tự của sâu str từ vị trí 2 -> 4 
  print(str[2]) - cắt kí tự của sâu str từ vị trí 2 -> hết
- xâu ký tự chiếm mấy dòng thì kết quả cũng in ra như vậy
- cắt chuỗi theo bước nhảy
  strSo = '123456789'
  strSoLe = strSo[0::2] - 0 là vị trí 2 là bước nhảy               => 2468
  strSoChan = strSo[1::2] - 1 là vị trí bắt đầu , 2 là bước nhảy   => 13579

'''


###
'''Ép kiểu 
- nguyên - int(x)
- thập phân - float(x)
- string - str(x)

s = '222211'
a = int(s)

- ép từ thực sang nguyên - mất hết thập phân 
- ép xâu sang nguyên mà xâu k có chả chữ cái sẽ sai
'''


