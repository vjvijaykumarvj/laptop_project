# Has-A RelationShip
class Car:
    #Constructor define for Employee Class
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    # instance Methoc Define For Employee
    def Car_details(self):
        print('Car brand : {}, Car Price is : {}, Card Color : {}'.format(self.brand,self.price,self.color))
class Employee():
    def __init__(self, eno, name, age):
        self.eno = eno
        self.name = name
        self.age = age
        self.car = Car('Innova', 'Iv.100','Red' )
    def Employee_info(self):
        print('My eno is : {}'.format(self.eno))
        print('My name is : {}'.format(self.name))
        print('My age is : {}'.format(self.age))
        print('My Card Details is : {}'.format(self.car))
obj = Employee(1001, 'vijay', 25)
obj.Employee_info()


