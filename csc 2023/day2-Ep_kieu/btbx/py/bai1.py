

def tinh_tien(SoLuong, DonGia):
    return SoLuong*DonGia

if __name__ == '__main__':
    SoLuong = eval(input('Nhập vào số lượng : '))
    DonGia = eval(input('Nhập vào đơn giá : '))
    res = f'Giá tiền cần thanh toán : {tinh_tien(SoLuong, DonGia):,}VND'
    print(res)