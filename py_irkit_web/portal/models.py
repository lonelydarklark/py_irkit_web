from django.db import models


# Create your models here.
class RawData(models.Model):
    id = models.IntegerField()
    time = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    di = models.FloatField()

    def __str__(self):
        return '{time}: {temperature}, {humidity}, {pressure}, {di}'\
            .format(time=self.time, temperature=self.temperature, humidity=self.humidity, pressure=self.pressure, di=self.di)

