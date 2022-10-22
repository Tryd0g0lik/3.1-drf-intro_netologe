# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView

from measurement.models import Measurement
from .serializers import SensorSerializers

@api_view(['GET',])
def api_gradus(request):
	measurement = Measurement.objects.all()
	ser = SensorSerializers(measurement, many=True)
	return Response(ser.data )