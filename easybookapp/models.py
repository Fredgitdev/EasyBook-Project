from django.db import models

# Create your models here.
#one way booking model
class OneWayBooking(models.Model):
    full_name = models.CharField(max_length=200)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    number_of_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.full_name} - {self.departure_date}"

#bus hiring model
class BusHiring(models.Model):
    full_name = models.CharField(max_length=200)
    pick_up_location = models.CharField(max_length=200)
    drop_off_location = models.CharField(max_length=200)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    contact = models.CharField(max_length=15)  # To accommodate phone numbers
    bus_type = models.CharField(max_length=200)
    seat_capacity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name} - {self.pick_up_date} - {self.bus_type}"


#contact model
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


#User's Registration Model
class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title