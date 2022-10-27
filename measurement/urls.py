from django.urls import path

from measurement.views import *

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
	path('', api_gradus.as_view()),
]
