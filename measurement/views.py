# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView

from measurement.models import Measurement, Sensor
from .serializers import SensorSerializers, MeasurementSerializer

@api_view(['GET',])
def api_gradus(request):
	sensor = Sensor.objects.all()
	# measurement = Measurement.objects.all()
	sen = SensorSerializers(sensor, many=True)
	# mean = MeasurementSerializer(measurement, many=True)


	ser = sen.data # + mean.data
	return Response(ser )