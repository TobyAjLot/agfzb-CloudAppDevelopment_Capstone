from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
# - Name
    name = models.CharField(max_length=200)
# - Description
    description = models.CharField(max_length=500)
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
    def __str__(self):
            return "Name: " + self.name + ", " + \
                "Description: " + self.description
                    


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    CAR_TYPE_CHOICES = [
        ("SE","Sedab"), 
        ("SU","SUV"), 
        ("WG","WAGON")
        ]
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Name
    name = models.CharField(max_length=200)
# - Dealer id, used to refer a dealer created in cloudant database
    dealer_id = models.IntegerField()
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    type = models.CharField(max_length=200, choices=CAR_TYPE_CHOICES)
# - Year (DateField)
    year = models.DateField()
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
    def __str__(self):
        return "Name: " + self.name + ", " + \
                "Car Make: " + self.car_make + ", " + \
                    "Year: " + self.year


# <HINT> Create a plain Python class `CarDealer` to hold dealer data



# <HINT> Create a plain Python class `DealerReview` to hold review data
