dict_Contact = {
    'chung':'012345',
    'đăng':'041234',
    'an':'542341',
    'huyền':'857308'
}

while True:
    print('\nCHƯƠNG TRÌNH QUẢN LÝ DANH BẠ ĐIỆN THOẠI')
    print(f' 1: Xem danh bạ\n 2: Tra cứu thông tin\n 3: Thêm thông tin\n 4: Kết thúc')
    ChucNang = input('Chọn Chức Năng : ')
    if ChucNang =='1':
        print('Xem Danh Bạ ')
        print('-'*50)
        print('Tên Khách Hàng'.ljust(35), 'Điện Thoại'.rjust(14))
        print('-'*50)
        for ten,sdt  in dict_Contact.items():
            strInfor = f'{ten:35} {sdt.rjust(14)}' # cho chuỗi dài ra
            print(strInfor)
        print('-'*50)
    elif ChucNang=='2':
        print('Tra Cứu Thông Tin')
        tenTC = input('Nhập vào thông tin cần tra cứu : ')
        res = dict_Contact.get(tenTC)
        if res == None:
            KQTC = 'Không có thông tin này trong danh bạ'
        else:
            KQTC = f'{tenTC:35} {dict_Contact[tenTC].rjust(14)}'
        print(KQTC)
    elif ChucNang =='3':
        print('Thêm Thông Tin')
        add_Name = input('Nhập vào tên cần thêm : ')
        if dict_Contact.get(add_Name) ==None:
            add_Phone = input('Nhập vào số điện thoại muốn thêm : ')
            dict_Contact[add_Name] = add_Phone
            print('Đã thêm thông tin thành công')
        else:
            print('Lỗi: Tên Liên lạc đã tồn tại')
    else: 
        print('Đã thoát khỏi chương trình')
        break

