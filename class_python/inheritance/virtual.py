'''
- Trong Python, không có từ khóa "virtual" như trong một số ngôn ngữ lập trình khác (ví dụ như C++). Tuy nhiên, Python tự động hỗ trợ khái niệm tương tự với "virtual" thông qua cơ chế kế thừa và đa hình mặc định của nó. 
- Hãy để tôi giải thích chi tiết hơn:
  + Tất cả các phương thức trong Python đều "virtual" theo mặc định:
    +) Khi bạn ghi đè một phương thức trong lớp con, Python sẽ tự động sử dụng phiên bản ghi đè này khi gọi phương thức trên một đối tượng của lớp con.
   
  + Đa hình động:
    +) Python sử dụng đa hình động, có nghĩa là phương thức được gọi được xác định tại thời điểm chạy dựa trên loại thực tế của đối tượng

'''

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_speak(dog)
make_speak(cat)