from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ('graduses', 'date')

class SensorMeasurementSerializers(serializers.ModelSerializer):
	measure_data = MeasurementSerializer(read_only=True, many=True)

	class Meta:
		model = Sensor
		fields = ('name', 'description', 'measure_data')

	# def create(self, **validated_data):
	# 	measures_data = validated_data.pop('measure_data')
	# 	sensor = Sensor.objects.create(**validated_data)
	# 	for measure_data in measures_data:
	# 		Measurement.objects.create(sensor=sensor, **measures_data)
	# 	return sensor

