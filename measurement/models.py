from django.db import models
from datetime import datetime

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
	name = models.CharField(max_length=50, null=True)
	description = models.TextField(max_length=1000)


class Measurement(models.Model):
	id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,
	                              related_name='measure_data',
	                              verbose_name='Данные')
	graduses = models.FloatField(verbose_name='Градус')
	date = models.DateTimeField(auto_now=True)