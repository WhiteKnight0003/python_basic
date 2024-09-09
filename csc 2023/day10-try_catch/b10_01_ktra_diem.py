try:
    dtb=float(input('Nhập điểm trung bình : '))
    assert dtb>=0 and dtb <=10, 'Điểm trung bình phải từ 0 -> 10'
    # dùng assest để cố định miền giá trị đúng
except ValueError: 
    print(f'Lỗi: Điểm trung bình phải nhập là số ')
    # valueError : lỗi giá trị k đúng định dạng
    # errMes: 1 biến mình đặt
except AssertionError as errMes:
    print('>>> Lỗi: ',errMes)
else: 
    if dtb>=8:
        xl='Giỏi'
    elif dtb>=6.5:
        xl='Khá'
    elif dtb>=5:
        xl='Trung Bình'
    elif dtb>=3.5:
        xl='Yếu'
    else:
        xl='Kém'
    print(xl)    

'''
Nhập điểm trung bình : rưerew
Lỗi: Điểm trung bình phải là số . could not convert string to float: 'rưerew'
'''