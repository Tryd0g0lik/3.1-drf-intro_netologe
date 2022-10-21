from django.urls import path

from measurement.views import api_gradus

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
	path('', api_gradus),
]
