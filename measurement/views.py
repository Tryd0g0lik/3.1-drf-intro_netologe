# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import generics
from measurement.models import *
from .serializers import *

# @api_view(['GET',])
# def api_gradus(request):
# 	sensor = Sensor.objects.all()
# 	sen = SensorSerializers(sensor, many=True)
# 	ser = sen.data # + mean.data
# 	return Response(ser )

class api_gradus(generics.ListCreateAPIView):
	queryset = Sensor.objects.all()
	serializer_class=SensorMeasurementSerializers


class api_gradus(APIView):
	def get(self, request):
		queryset = Sensor.objects.all()
		serializer_class=SensorMeasurementSerializers(queryset, many=True)
		return Response(serializer_class.data)