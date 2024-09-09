# mở tập tin
'''
file_object = open(fine_name [, access_mode][, buffering])

- file_name : tên tập tin sẽ truy cập
- access_mode: chế độ mở tập tin : read, write , append,...
- buffering : 1: có thể sử dụng buffer
              0: không thể sử dụng buffer
              >1: buffer size
              <0: default size


- access_mode :
r : only read file
w : only write file
a : append : thêm nội dung vào file


- attribute of file object
Attribute               |  Description
file.closed             | Trả về TRUE nếu tệp bị đóng, false nếu không
file.mode               | Trả về chế độ truy cập với tệp đã được mở
file.name               | returns name of the file
'''

#read
# f = open('data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee\Text.txt','r',encoding='utf-8') # nếu file tiếng việt thì cần utf8 để đọc
# str = f.read()
# f.close()
# print(str)

#read_seek - đọc ra n kí tự đầu 
# seek(offset, whence)
''' whence
0 (hay os.SEEK_SET): Con trỏ sẽ được đặt tính từ đầu file.
1 (hay os.SEEK_CUR): Con trỏ sẽ được đặt tính từ vị trí hiện tại của con trỏ.
2 (hay os.SEEK_END): Con trỏ sẽ được đặt tính từ cuối file.
'''
f = open('data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee\Text.txt','r',encoding='utf-8') # nếu file tiếng việt thì cần utf8 để đọc
str = f.read(5) #fdsfd
f.seek(9,0)
str2= f.read(3) # đọc từ vị trí 9 thêm 3 kí tự 
f.close()
print(str2)


#readlines - trả kq về 1 list - mỗi dòng là 1 phần tử
# k = open('data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee\Text.txt','r',encoding='utf-8') # nếu file tiếng việt thì cần utf8 để đọc
# str1 = k.readlines()
# print(str1)
# k.close()


# viết ngắn lại
# with open('data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee\Text.txt','r',encoding='utf-8') as f:
#     ListStr = f.readlines()
# print(ListStr)


#write 
# tenTapTin = input('Nhập vào tên tập tin : ')
# strNoiDung = input('Nhập nội dung : ')

# txtName = f'data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee/{tenTapTin}.txt'
# # mở tập tin để ghi - tạo mới - nó sẽ đè vào file đang có hiện tại
# with open(txtName,'w',encoding='utf-8') as f:
#     f.write(strNoiDung)
# print('Ghi thành công')


#writelines_list - ghi vào hẳn 1 list
# listStr = [
#     'fdsfdsfg\n',
#     'gfdgfda\n',
#     'fdfffff'
# ]
# tenTapTin = input('Nhập vào tên tập tin : ')

# txtName = f'data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee/{tenTapTin}.txt'
# with open(txtName,'w',encoding='utf-8') as f:
#     f.writelines(listStr)
# print('Ghi thành công')


# append - ghi thêm nếu file đã tồn tại
# tenTapTin = input('Nhập vào tên tập tin : ')
# listStr = [
#     'fdsfdsfg\n',
#     'gfdgfda\n',
#     'fdfffff'
# ]
# txtName = f'data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee/{tenTapTin}.txt'
# with open(txtName,'a',encoding='utf-8') as f:
#     f.writelines(listStr)
# print('Ghi thành công')