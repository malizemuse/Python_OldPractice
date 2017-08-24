class Car(object):
    ''' A simple Car class '''

    condition = "new"
    def __init__(self, model, color, mpg):
        ''' Constructor '''
        self.model = model
        self.color = color
        self.mpg   = mpg
  
    def display_car(self):
        ''' Displays color, model, and mpg of car '''
        print "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        ''' A new car driven changes condition to "used" '''
        self.condition = "used"
    
class ElectricCar(Car):
    ''' Subclass of the Car class '''
  
    def __init__(self, model, color, mpg, battery_type):
        ''' Constructor '''
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
  
    def drive_car(self):
        ''' Overrides the drive car method in Car superclass '''
        self.condition = "like new"
 

# Sample creation of object and use of methods
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition