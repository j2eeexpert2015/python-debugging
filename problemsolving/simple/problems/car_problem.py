class Car:
    def init (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer} miles on it.")

car = Car('audi','a4',2020)
print(car.get_description())
car.read_odometer()

