# gọi ra nhiều đối tượng 1 lúc

# dùng list
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says: Woof!")

dogs = [Dog(f"Dog_{i}") for i in range(0,11)] # tạo ra 10 con chó

# duyệt 
for dog in dogs:
    dog.bark()

# xóa theo vị trí
del dogs[2] # xóa com ở vị trí 3

# xóa theo value
dog_to_remove = dogs[5] # xóa con chó thứ 6
dogs.remove(dog_to_remove)

# xóa theo điều kiện
dogs = [dog for dog in dogs if dog.name !="Dog_4"] ## Xóa con chó có tên "Dog_4"

# dùng pop() để xóa và trả về con chó bị xóa:
removed_dog = dogs.pop(2)  # Xóa và trả về con chó ở vị trí thứ 3 (index 2)
print(f"Removed: {removed_dog}")

for dog in dogs:
    dog.bark()