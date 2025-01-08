from django.db import models

# Create your models here.
# metrics/models.py
from django.db import models

class SystemMetrics(models.Model):
    cpu_usage = models.FloatField()
    ram_usage = models.FloatField()
    disk_usage = models.FloatField()
    uptime = models.FloatField()
    temperature = models.FloatField(null=True, blank=True)  # Optional
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Metrics at {self.timestamp}'


class Threshold(models.Model):
    cpu_usage_threshold = models.FloatField(default=80.0)  # Default 80%
    ram_usage_threshold = models.FloatField(default=8.0)  # Default 8 GB
    disk_usage_threshold = models.FloatField(default=10.0)  # Default 10 GB
    uptime_threshold = models.FloatField(default=24.0)  # Default 24 hours
    temperature_threshold = models.FloatField(default=75.0)  # Default 75°C

    def __str__(self):
        return "Threshold Settings"