from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ('id', 'graduses', 'date')

	def update(self, instance, validated_data):
		instance.graduses = validated_data.get('graduses', instance.graduses)
		return instance

class SensorMeasurementSerializers(serializers.ModelSerializer):
	measure_data = MeasurementSerializer(read_only=True, many=True)
	# id_measure= serializers.IntegerField(max_value=40, min_value=-40)
	class Meta:
		model = Sensor
		fields = ('id', 'name', 'description', 'measure_data')


