from django.contrib import admin
from .models import SystemMetrics,Threshold
# Register your models here.
admin.site.register(SystemMetrics)

admin.site.register(Threshold)