from django.db import models

# Create your models here.


class Courier(models.Model):
    courier_id = models.CharField(primary_key=True, max_length=25)
    courier_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.courier_name


class Package(models.Model):
    package_id = models.CharField(primary_key=True, max_length=25)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    estimated_arrival_time = models.DateTimeField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
