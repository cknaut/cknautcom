from django.db import models
from gcharts import GChartsManager


class data_point(models.Model):
    #Temperature in Degrees Celsius
    temp = models.CharField(max_length=30)

    #Air Humidity in %
    hum = models.CharField(max_length=30)

    #Timestamp
    created = models.DateTimeField(auto_now_add=True)

    # register the GChartsManager as default manager for this model.
    objects = GChartsManager()

    class Meta:
        get_latest_by = "created"


# Create your models here.
