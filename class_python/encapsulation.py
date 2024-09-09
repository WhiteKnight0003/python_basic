# trong python để thuộc tính ở private thì dùng dấu _
# tính đóng gói
class Computer:
    def __init__(self):
        self._maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self._maxprice))

    def setMaxPrice(self, price):
        self._maxprice = price

C = Computer()
C.sell()

#change the price 
C._maxprice = 100
C.sell()

#using setter func
C.setMaxPrice(1992)
C.sell()

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Thuộc tính "private"

    def get_age(self):
        return self._age

- age ở đây là private , và phải dùng getter để truy xuất 
'''