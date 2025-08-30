class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f'Brand:{self.brand}, Model: {self.model}, Year: {self.year}')

car1 = Car('Toyota', 'Premio', 2017)
car1.car_info()