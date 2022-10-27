from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ('graduses', 'date')

class SensorMeasurementSerializers(serializers.ModelSerializer):
	measurement = MeasurementSerializer(read_only=True, many=True)

	class Meta:
		model = Sensor
		fields = ('name', 'description', 'measurement')




# class SensorSerializers(serializers.ModelSerializer):
#
# 	class Meta:
# 		model = Sensor
# 		fields = ('name', 'description', 'measurement')
#
#
# class MeasurementSensorSerializer(serializers.ModelSerializer):
# 	sensores = SensorSerializers(many=True, read_only=True)
# 	# sensores = serializers.StringRelatedField(many=True)
# 	class Meta:
# 		model = Measurement
# 		fields = ('graduses', 'date', 'sensores')