class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")
    
    def make_sound(self):
        return f"{self.name} says: Meow!"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")
    
    def make_sound(self):
        return f"{self.name} says: Woof!"

# Tạo 10 con mèo bằng cách gọi lớp Animal
cats = [Animal(f"Cat_{i}", "Cat") for i in range(1,11)]

for cat in cats:
    print(f"Name: {cat.name}, Species: {cat.species} , Make_sound: {cat.make_sound()}")
    # Name: Cat_1, Species: Cat , Make_sound: None
    # k thể kêu 

# Nếu bạn muốn các con mèo có thể kêu, bạn cần chuyển đổi chúng thành đối tượng Cat
cat_obj = [Cat(animal.name) for animal in cats]

for cat in cat_obj:
    print(f"{cat.make_sound()}")
