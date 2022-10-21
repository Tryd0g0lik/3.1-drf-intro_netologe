from rest_framework import serializers
from rest_framework import ListAPIView
# TODO: опишите необходимые сериализаторы
from .models import *

class MeasurementSerializers(serializers.ModelSerializer):

	class Meta:
		model = Measurement
		field = ('id_sensor', 'graduses', 'date')

