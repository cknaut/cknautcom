from django.db import models


class data_point(models.Model):
    #Temperature in Degrees Celsius
    temp = models.CharField(max_length=30)

    #Air Humidity in %
    hum = models.CharField(max_length=30)

    #Timestamp
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "created"


# Create your models here.
