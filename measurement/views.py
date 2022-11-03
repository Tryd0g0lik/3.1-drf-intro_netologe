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

