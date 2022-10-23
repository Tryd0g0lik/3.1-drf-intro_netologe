from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ('graduses', 'date')

class SensorSerializers(serializers.ModelSerializer):
	measurement = MeasurementSerializer(read_only=True, many=True)

	class Meta:
		model = Sensor
		fields = ('id', 'name', 'description', 'measurement')




