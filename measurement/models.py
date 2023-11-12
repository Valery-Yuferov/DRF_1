from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    sensor_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)


