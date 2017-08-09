class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()

    def read_odometer(self):
        print("this car has {}".format(self.odometer_reading) + "miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odomete_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")


    def increment_odometer(self, miles):
        self.odometer_reading += miles










mycar = Car("mitsubishi", "outback", "2015")




print(mycar.get_descriptive_name())