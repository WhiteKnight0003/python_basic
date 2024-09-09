# base class
# self là một tham số đặc biệt được sử dụng trong các phương thức của lớp. Nó đại diện cho thể hiện cụ thể của lớp mà phương thức đang được gọi trên đó. Cụ thể
class Animal:
    def eat(self):
        print("I can eat!")
    
    def sleep(self):
        print("I can sleep!")

#derived class
class Dog(Animal):
    def bark(self):
        print("I can bark! Woof woof !!")

# create object of the Dog class
dog1 = Dog()

#calling members of the base class 
dog1.eat()
dog1.sleep()

# calling member of the derived class 
dog1.bark()