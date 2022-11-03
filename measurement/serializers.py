from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ('id', 'graduses', 'date')

class SensorMeasurementSerializers(serializers.ModelSerializer):
	measure_data = MeasurementSerializer(read_only=True, many=True)

	class Meta:
		model = Sensor
		fields = ('id', 'name', 'description', 'measure_data')

