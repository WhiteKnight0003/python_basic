
def Gui_tiet_kiem(soTien, soThang, LaiXuat):
    tienLai = soTien*soThang*LaiXuat/(12*100)
    return soTien+tienLai 

if __name__ == '__main__':
    So_Tien_Gui = eval(input('Nhập vào số tiền : '))
    Thoi_Han = eval(input('Nhập vào thời hạn gửi : '))
    Lai_Xuat_Nam = eval(input('Nhập vào lãi xuất của năm nay : '))

    res = f'Số Tiền sau khi rút về là : {Gui_tiet_kiem(So_Tien_Gui,Thoi_Han,Lai_Xuat_Nam):,.3f}VND'
    print(res)