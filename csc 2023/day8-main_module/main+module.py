# from folder_name import file_name as tên_đại_diện
# or import folder.file as tên_đại_diện
import danhba as db

if __name__ == '__main__':
    dict_Contact = {
    'Chung':'012345',
    'Đăng':'041234',
    'An':'542341',
    'Huyền':'857308'
    }

    while True:
        print('\nCHƯƠNG TRÌNH QUẢN LÝ DANH BẠ ĐIỆN THOẠI')
        print(f' 1: Xem danh bạ\n 2: Tra cứu thông tin\n 3: Thêm thông tin\n 4: Kết thúc')
        ChucNang = input('Chọn Chức Năng : ')
        if ChucNang =='1':
           db. show_contact(dict_Contact)
        elif ChucNang=='2':
            name = input('Nhập vào tên cần tra cứu : ').strip().title()
            db.find_contact(dict_Contact,name)
        elif ChucNang =='3':
            add_Name = input('Nhập vào tên cần thêm : ').strip().title()
            add_Phone = input('Nhập vào số điện thoại muốn thêm : ').strip()
            db.add_contact(dict_Contact,add_Name,add_Phone)
        else: 
            print('Đã thoát khỏi chương trình')
            break

