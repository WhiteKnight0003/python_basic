#string
'''

s1 = '      Adasd fdEDa DfSBB        '
k1 = s1.capitalize() #    Adasd fdeda dfsbb        -     chỉ có chữ đầu dòng viết hoa
k2 = s1.upper() # -    viết hoa tòan str
k3 = s1.lower() # - viết thường toàn str
k4 = s1.title() #       Adasd Fdeda Dfsbb          - viết hoa từng kí tự sau khoảng trắng 
k5 = s1.strip() # cắt kí tự trong ngoặc ở 2 đầu    - nếu k có gì trong ngoặc thì mặc định là khoảng trắng
 
s2 = ',dsfsd,fsdfs,fsdfsd,đ,'
k6 = s2.strip(',') 
k7 = s2.lstrip(',') # 'dsfsd,fsdfs,fsdfsd,đ,'         cát kí tự trong ngoặc ở đầu bên trái 
k8 = s2.rstrip(',') # ',dsfsd,fsdfs,fsdfsd,đ'         cắt kí tự trong ngoặc ở đầu bên phải

s3 = """
Nước Nam Việt có vua Nam Việt,
Trên sách trời chia biệt rành rành.
Cớ sao Nam giặc dám hoành hành?
Rồi đây bay sẽ tan tành cho coi .
"""
print(s3) # trong comment như thế nào thì s3 như v
print(len(s3)) # đếm số kí tự
print(s3.count('Nam')) # đếm số kí tự trong ngoặc
print(s3.lower().count('n',3,20)) # đếm kí tự từ vị trí start = 3 đến vị trí end = 20

print(s3.replace('Nam','Nữ')) ## thay thế replace(từ cần thay , từ được thay thế)
print(s3.replace('Nam','Nữ',2)) # 2 ở đây là số kí tự sẽ được thay thế tính từ đầu dãy

i = s3.find(' ') # nếu k có trả về -1   or kết quả từ 0<= <= len(s)-1
print(i) # tìm kí tự ' ' và trả về vị trí đầu tiên nó xuất hiện
print(s3.find(' ',i+1))  # tìm kí tự ' ' và trả về vị trí đầu tiên nó xuất hiện từ vị trí i+1
print(s3.find('\n')) # trả về vị trí cuối cùng kí tự đó xuất hiện 



strSDt = '432432432'
k1 = strSDt.isdigit()  # true
k2 = strSDt.isnumeric() # true
# 2 hàm trên đều check xem str có toàn số không 


strST = '15000VND'
strMS = 'ASKD'
k3 = strMS.isalpha() #check xem có phải toàn chữ cái không - chỉ tính chữ bthg chứ k tính kí tự đặc biệt
k4 = strST.isalpha()
k5 = strST.isalnum() #check chuỗi xem có phải nó vừ có số , vừa có chữ không
k6 = strMS.isupper() # check xem chuỗi có in hoa không
k7 = strMS.islower() # check xem chuỗi có in thường không
print()

'''

'''
strD ='abVC'
str1 = strD.center(20)   #'        abVC        '   đẩy vào giữa của khoảng 20 kí tự
str2 = strD.center(20,'*') #'********abVC********'
str3 = strD.ljust(20) # 'abVC                '- căn trái 
str4 = strD.rjust(20) # '                abVC'- căn phải
print()
'''

''' - lấy kí tự từ vị trí start -> end -1
name = "dsds sàdasdas"
print(name[0:3])
'''



'''split() - cắt chuỗi theo kí tự tròng ngoặc
'''
strHoTen = 'lê      Tiến          Chung'
listHoten = strHoTen.split() # dùng 1 list để chứa kq - ['lê', 'Tiến', 'Chung']
strSo='12,13,14,15,16,17,18,19' 
listSo1 = strSo.split(',') # ['12', '13', '14', '15', '16', '17', '18', '19'] cắt full
listSo2 = strSo.split(',',maxsplit=3) # ['12', '13', '14', '15,16,17,18,19'] - chỉ cắt tối đa 3 dấu ,

'''join - gắn các kí tự '''
strN = ','.join(listHoten) # 'lê,Tiến,Chung' gắn các kí tự thành 1 str theo dấu
print()