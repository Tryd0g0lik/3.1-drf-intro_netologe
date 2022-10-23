from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *

class SensorSerializers(serializers.ModelSerializer):

	class Meta:
		model = Sensor
		fields = ('id', 'name', 'description')

class MeasurementSerializer(serializers.ModelSerializer):

	class Meta:
		model = Measurement
		fields = ('id', 'id_sensor', 'graduses', 'date')


