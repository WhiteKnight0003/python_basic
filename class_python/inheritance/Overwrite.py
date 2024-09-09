# Overwrite thường đề cập đến việc thay thế hoàn toàn một thuộc tính hoặc phương thức của lớp cha, không giữ lại bất kỳ chức năng nào của phiên bản gốc

class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        print("Completely new implementation")

child = Child()
child.method()