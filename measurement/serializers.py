from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *

class SensorSerializers(serializers.ModelSerializer):

	class Meta:
		model = Sensor
		fields = ('id', 'name', 'description')


