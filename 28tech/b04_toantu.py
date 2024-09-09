''' Các loại toán tử
- Toán tử gán             -> Assignment operator 
- Toán tử toán học        -> Arithmetic operator
- Toán tử so sánh         -> Comparison operator
- Toán tử logic           -> Logical operator
- toán tử nhận dạng       -> Identity operator
- toán tử thành viên      -> Membership operator
- toán tử bit             -> Bitwise operator
'''

### Toán tử gán a = b ; gán giá trị b cho a
# gán cho nhiều biến a,b ,c = 100, 200, "28tech"  -> các biến có thể chữa kiểu dữ liệu khác nhau
# để hoán đổi 2 giá trị của 2 biến a, b = b, a


### toán tử toán học
'''
+   
-  
*
/   - chia thập phân 3/2 = 1.5
//  - chia nguyên  15//2 = 7
%   - chia dư   15%2 = 1
**  - lũy thừa  2**3 = 8

'''


### toán tử so sánh - kết quả phép so sánh trả về true or false
'''
== 
>
>=
<
<=
!= 
'''


### toán tử logic and, or , not - dùng luôn 3 cno
'''
((x>20) and (x<= 30))
((x>20) or (x<= 30))
not(x<=30)
'''


### toán tử nhận dạng - so sánh 2 đối tượng(địa chỉ ,vùng nhớ mà chúng sử dụng) chứ k phải so sánh 2 giá trị
# is : trả về true nếu 2 đối tượng giống nhau 
# is not : trả về true nếu 2 đối tượng khác nhau 
'''
a = [1,2,3]
b = [1,2,3]
print(a is b) -> false - vì các list này có thành phần như nhau nhưng id của nó khác nhau nên false
'''


### toán tử nhận dạng - để ktra sự tồn tại của 1 đối tượng trong list , xâu, ...
# in : trả về true nếu đối tượng tồn tại    'a' in 'abcd' -> true
# not in : trả về true nếu đối tượng không tồn tại    'r' not in  'abcd' -> true