from django.urls import path

from measurement.views import *

urlpatterns = [
	path('', api_gradus.as_view()),
	path('sensor/<pk>/', Api_gradusViewSet.as_view()),
	path('meas/', MeasurementAllrViewSet.as_view()),
	path('meas/<pk>/', MeasurementViewSet.as_view()),
	path('meas/', MeasurementViewSet.as_view()),
]
