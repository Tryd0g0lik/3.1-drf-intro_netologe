from django.db import models
from datetime import datetime

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
	name = models.CharField(max_length=50, blank=True,
	                        default='sensor',
	                        verbose_name='Модель',
	                        help_text='Название модели.')
	description = models.TextField(max_length=1000,
	                               verbose_name='Описание',
	                               blank=True,
	                               help_text='Ваше примичание к прибору.')

	def __str__(self):
		return '%s (%s)' % (self.name, self.description)

	class Meta:
		verbose_name='Сенсор'
		verbose_name_plural='Сенсоры'
		ordering=['id']



class Measurement(models.Model):


	graduses = models.FloatField(verbose_name='Градус',
	   default=00.0,
	   help_text='Измеряемая температура в цельсиях.'
	   )
	date = models.DateTimeField(auto_now=True,
		verbose_name='Дата и время',
		help_text='Дата и время проводимых измерений.'
		)
	id_sensor = models.ForeignKey(
		Sensor, on_delete=models.PROTECT,
		db_index=True,
		related_name='measure_data',
		verbose_name='Данные',
		null=True
		)

	def __str__(self):
		dates = '%s записано в таблицу %s' % (self.graduses, self.date,)
		return dates

	class Meta:
		verbose_name = 'Измерение'
		verbose_name_plural = 'Измерения'
		ordering = ['-date',]