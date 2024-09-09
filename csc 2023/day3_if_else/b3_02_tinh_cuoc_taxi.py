'''
- Cước phí của xe 4 chỗ :
+ Giá mở cửa 11.000 đồng/ 0.8 km
+ Trong phạm vi 30km 15.300 đồng/km
+ Từ km thứ 31 trở đi 12.100 đồng/km
- Cước phí của xe 7 chỗ :
+ Giá mở cửa 12.000 đồng/ 0.8 km
+ Trong phạm vi 30km 16.100 đồng/km
+ Từ km thứ 31 trở đi 13.800 đồng/km

Tiền chờ: 5 phút đầu miễn phí, từ phút thứ sáu trở đi là 750đ/phút

Yêu cầu:
- Người dùng nhập vào loại xe (4 hoặc 7), số km di chuyển và thời gian chờ (Input)
- Chương trình sẽ tính: Tiền chờ, Tiền di chuyển, Tiền cước (Tiền cước = Tiền chờ + Tiền di chuyển)
và in ra kết quả (Output).

'''

while True:
    try:
        xe = int(input('Nhập vào số chỗ ngồi của xe : '))
        assert xe==4 or xe==7, 'Chỉ nhập xe 4 chỗ hoặc xe 7 chỗ'
        
        km = float(input('Nhập vào số km di chuyển : '))
        assert km >=0 ,'Số km di chuyển phải >=0'

        time_cho = eval(input('Nhập vào số thời gian chờ : '))
        assert time_cho>=0,'Thời gian chờ  phải >=0'
        '''
        except ValueError as errNumber:
            print(f'Lỗi : dữ liệu nhập không đúng\n{errNumber}')
        except AssertionError as errNumber:
            print('>>>Lỗi : ',errNumber)
    '''
    #thay thế cho except ở trên
    except Exception as errNumber: # tổng quát hết mọi loại lỗi , nhưng nếu đc nên bắt riêng từng cái
        print(f'Lỗi : dữ liệu nhập không đúng\n{errNumber}')
    else:
        if xe==4:
            gia_mo_cua = 11000
            gia_trong_30km_dau = 15300
            gia_tu_km_thu_31 = 12100 
        else :
            gia_mo_cua = 12000
            gia_trong_30km_dau = 16100
            gia_tu_km_thu_31 = 13800 

        tien_cho=0
        if time_cho >=5 :
            tien_cho+=(time_cho -5)*750
            
        if  km<=0.8:
            tienxe = gia_mo_cua
        elif km<=30:
            tienxe = gia_mo_cua + gia_trong_30km_dau*(km-0.8)
        else:
            tienxe = gia_mo_cua + gia_trong_30km_dau*(30-0.8) + gia_tu_km_thu_31*(km-30)

        tong_tien = tien_cho + tienxe
        print(tong_tien)
    traloi = input('Bạn có muốn tiếp tục [y|n] : ').strip().lower() #strip()- xóa khoảng trắng 2 đầu
    if traloi!='y':
        break

