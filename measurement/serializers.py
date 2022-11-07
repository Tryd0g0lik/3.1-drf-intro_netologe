from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):

	class Meta:
		model = Measurement
		fields = ("id", "graduses", 'id_sensor')
		# exclude = ['id_sensor']


class SensorMeasurementSerializers(serializers.ModelSerializer):
	name = serializers.CharField()
	measure_data = MeasurementSerializer(many=True, read_only=True)

	class Meta:
		model = Sensor
		fields = ("id", "name", "measure_data")



