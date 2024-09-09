
def show_contact(dict_Contact):
    print('Xem Danh Bạ ')
    print('-'*50)
    print('Tên Khách Hàng'.ljust(35), 'Điện Thoại'.rjust(14))
    print('-'*50)
    for ten,sdt  in dict_Contact.items():
        strInfor = f'{ten:35} {sdt.rjust(14)}' # cho chuỗi dài ra
        print(strInfor)
    print('-'*50)

def find_contact(dict_Contact,name):
    print('Tra Cứu Thông Tin')
    res = dict_Contact.get(name)
    if res == None:
        KQTC = 'Không có thông tin này trong danh bạ'
    else:
        KQTC = f'{name:35} {dict_Contact[name].rjust(14)}'
    print(KQTC)

def add_contact(dict_Contact, add_name, add_phone):
    print('Thêm Thông Tin')
    if dict_Contact.get(add_name) ==None:
        dict_Contact[add_name] = add_phone
        print('Đã thêm thông tin thành công')
    else:
        print('Lỗi: Tên Liên lạc đã tồn tại')

