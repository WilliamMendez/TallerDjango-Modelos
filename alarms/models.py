from django.db import models
from measurements.models import Measurement

class Alarm(models.Model):
    name = models.CharField(max_length=10, default='none')
    measurements = models.ManyToManyField(Measurement)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name