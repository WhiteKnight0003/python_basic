# super() là một hàm tích hợp trong Python được sử dụng để gọi phương thức của lớp cha từ lớp con
class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        super().method() # Gọi phương thức của lớp cha
        print("Child method")

'''Ưu điểm của super()
- Hỗ trợ kế thừa đa hình
- Duy trì thứ tự MRO (Method Resolution Order)
- Tránh gọi trực tiếp phương thức của lớp cha, giúp code linh hoạt hơn
'''