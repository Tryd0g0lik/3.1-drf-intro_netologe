from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ('__all__')


class SensorMeasurementSerializers(serializers.ModelSerializer):
	measure_data = MeasurementSerializer(many=True, read_only=True)

	class Meta:
		model = Sensor
		fields = ('__all__')


