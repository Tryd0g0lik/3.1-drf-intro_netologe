# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *

class api_gradus(ModelViewSet, ):
	queryset = Sensor.objects.all()
	serializer_class=SensorMeasurementSerializers

class Api_gradusViewSet(ModelViewSet, ):
	queryset = Sensor.objects.all()
	serializer_class = SensorMeasurementSerializers

class MeasurementAllrViewSet(ModelViewSet,):
	queryset=Measurement.objects.all()
	serializer_class = MeasurementSerializer

class MeasurementViewSet(ModelViewSet,):
	queryset=Measurement.objects.all()
	serializer_class = MeasurementSerializer
	print(serializer_class.data)

class MeasurementViewSet(ModelViewSet, ):
	queryset=Measurement.objects.all()
	serializer_class = MeasurementSerializer



