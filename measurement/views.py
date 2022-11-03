# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import generics
from measurement.models import *
from .serializers import *

class api_gradus(generics.ListCreateAPIView):
	queryset = Sensor.objects.all()
	serializer_class=SensorMeasurementSerializers

class Api_gradusViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorMeasurementSerializers

class MeasurementAllrViewSet(generics.ListCreateAPIView):
	queryset=Measurement.objects.all()
	serializer_class = MeasurementSerializer

class MeasurementViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset=Measurement.objects.all()
	serializer_class = MeasurementSerializer

