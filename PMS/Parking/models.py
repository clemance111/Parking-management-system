from django.db import models
from django.utils import timezone
# Create your models here.


class Car(models.Model):
    plate_number = models.CharField(max_length=7, unique=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.plate_number


class Parking(models.Model):
    slots = models.IntegerField()
    name = models.CharField(max_length=50, default="chic")
    price = models.IntegerField()

    class Meta:
        verbose_name = "Parking"
        verbose_name_plural = "Parkings"

    def __str__(self):
        return self.name


class CarParking(models.Model):
    car = models.ForeignKey(Car, related_name="parkings",
                            on_delete=models.CASCADE)
    parking = models.ForeignKey(
        Parking, related_name="cars", on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CarParking"
        verbose_name_plural = "CarParkings"

    def __str__(self):
        return self.parking.name
    @property
    def get_price(self):
        remaining_time = timezone.now()-self.entry_time
        hour = remaining_time.seconds//3600
        return self.parking.price*hour