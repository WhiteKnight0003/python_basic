# đổi tiên và xóa tập tin với module os

# đổi tên với rename() và xóa file với remove()
'''
os.rename(current_file_name, new_file_name)
'''
import os
# os.rename('E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee\dsds.py', 'E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee\Rename.txt')
#os.remove('E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee\Rename.txt')

thumucHienHanh = os.getcwd()
listTenTapTin = os.listdir('E:\Data Specialized\data science\Course_1---Fundamentals_of_Python\csc 2023\day11\Fileee') # đưa ra các tệp con trong thư mục Fileee
print(listTenTapTin)


# xóa màn hình - nội dung trong terminal
# for mac, linux (here , os.name is 'posix)
# os.system('clear')
# os.system('clear')

#window
# os.system('cls')
# os.system('cls' if os.name == 'nt' else 'clear')  - chuyển đổi khi dùng mac , linux và window
os.system('cls')
print('dsadasd')