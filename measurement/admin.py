from django.contrib import admin

# Register your models here.
from measurement.models import *

class SensorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
	list_display_links = ('id', 'name')
	list_filter=('name',)
	search_fields=('name',)

class MeasurementAdmin(admin.ModelAdmin):
	list_display=('id', 'id_sensor', 'graduses', 'date')
	list_display_links=('id_sensor',)
	list_filter=('id_sensor', 'graduses', 'date')
	search_fields=('id_sensor', 'graduses', 'date')

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Measurement, MeasurementAdmin)