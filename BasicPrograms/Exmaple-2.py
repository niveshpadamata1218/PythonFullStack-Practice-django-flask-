class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(self.year,self.make,self.model)

my_car=Car("nivesh","benx",2034)
my_car.display()