from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ('__all__')



	# def update(self, measure_data, validated_data):
	# 	validated_data.get('graduses')
	# def update(self, measure_data, validated_data):
	#
	# 	measure_data.id_sensor = validated_data.get('id_sensor',
	# 	                                        measure_data.id)
	# 	measure_data.graduses = validated_data.get('graduses',
	# 	                                measure_data.graduses)
	# 	measure_data.save()
	# 	return measure_data

class SensorMeasurementSerializers(serializers.ModelSerializer):
	measure_data = MeasurementSerializer(many=True, read_only=True)
	# graduses = serializers.IntegerField(min_value=-50,
	#                                     max_value=60,
	#                                     )
	# graduses = serializers.IntegerField()
	# measure_ = measure_data['graduses']
	# print(measure_data.data)


	class Meta:
		model = Sensor
		fields = ('__all__')

	def update(self, instance, validated_data):

		# instance.id_sensor = validated_data.get(
		# 	'id_sensor',
		# 	instance.id
		# 	)
		# instance.measure_data.graduses = validated_data.set(
		# 	"measure_data",
		# 	instance.measure_data
		# 	)
		instance.measure_data.set(["measure_data"])
		instance.save()
		return instance

