from django.urls import path
from rest_framework.routers import  DefaultRouter
from measurement.views import *

router = DefaultRouter()
router.register('sensor', Api_gradusViewSet)
router.register('meas', MeasurementViewSet)

urlpatterns = [
] + router.urls


