'''
viết Ct xét tuyển sinh vào lớp ...
Nếu điểm >=5 đậu , ngược lại - rớt

#1 - thu thập thông tin
hoTen = input('Nhập họ tên : ')
diem = float(input('Nhập vào điểm : '))
Giay_moi_nhap_hoc = f'Giấy mời nhập học của thí sinh : {hoTen}'

#2 - xử lý & kết xuất
if diem>=5.0:
    print('đậu')
else :
    print('rớt')

'''

''' giải ptb1 ax +b=0
'''
try: # ép kiểu của các biến cũng phải khác nhau nếu k lối báo ra sẽ sai
    a = float(input('Nhập vào hệ số a : '))
    b = eval(input('Nhập vào hệ số b : '))
except ValueError: # k đc viết 2 kết quả của 2 biến trong cùng 1 lỗi và kể cả có tách ra cũng v
    print('Hệ số của a phải là số ')
    #print('Hệ số của b phải là số ') - sai
except NameError:
    print('Hệ số của b phải là số ')
else:
    if a!=0:
        res = -b/a
        print(f'Nghiệm của phương trình là : {res:.2f}')
    elif b==0:
        print(f'Phương trình có vô số nghiệm')
    else: 
        print(f'Phương trình vô nghiệm')