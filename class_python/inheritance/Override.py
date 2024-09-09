#Override là việc định nghĩa lại một phương thức trong lớp con mà đã được định nghĩa trong lớp cha
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self): # ghi đè phương thức của lớp cha
        print("Woof!")

dog = Dog()
dog.make_sound()

''' Đặc điểm của override
- Phương thức trong lớp con có cùng tên và tham số với phương thức trong lớp cha
- Cho phép lớp con cung cấp cài đặt cụ thể cho phương thức của lớp cha
- Hữu ích trong việc thực hiện tính đa hình
'''