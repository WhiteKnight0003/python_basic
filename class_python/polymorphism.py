# tính đa hình - mục đích là phân biệt kết quả 
class Polygon:
    #method to render a shape
    def render(self):
        print("Rendering polygon ...")

class Square(Polygon):
    #renders Square
    def render(self):
        print('Rendering Square ...')

class Circle(Polygon):
    #renders circle
    def render(self):
        print('Render Circle ...')

#create an object of Square
s1 = Square()
s1.render()

#create an object of Circle
s2 = Circle()
s2.render()


# kế thừa đơn (Single Inheritance) - 1 lớp con kế thừa từ 1 lớp cha
'''
class Parent:
class Child(Parent):
'''

# kế thừa đa cấp(Multilevel Inheritance) - 1 lớp kế thừa từ 1 lớp con, tạo thành 1 chuỗi kế thừa
'''
class Grandparent:
class Parent(Grandparent):
class child(Parent):
'''

# kế thừa đa hình (Multiple Inheritance) - 1 lớp con kế thừa từ nhiều lớp cha
'''
class Father:
class Mother:
class Child(Father, Mother):
'''

# kế thừa phân cấp (Hierarchical Inheritance) - nhiều lớp con kế thừa từ 1 lớp cha
'''
class Parent:
class Child1(Parent):
class Child2(Parent):
'''

# kế thừa lai (Hybrid Inheritance) - kết hợp 2 or nhiều loại kế thừa
'''
class A:
class B(A):
class C(A):
class D(B,C):
'''

# kế thừa mixin - sử dụng các lớp nhỏ độc lập để thêm chức năng vào lớp chính
'''
class Mixin1:
    def method1(self):
class Mixin2:
    def method2(self):
class Myclass (Mixin1, Mixin2):
'''