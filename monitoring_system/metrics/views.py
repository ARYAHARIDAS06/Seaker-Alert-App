# metrics/views.py
from django.shortcuts import render,redirect
from .utils import get_system_metrics, collect_metrics  # Assuming you have both functions
from .models import SystemMetrics,Threshold
from django.http import JsonResponse
def dashboard(request):
    # Collect metrics using a utility function
    metrics_data = get_system_metrics()  # Assuming this returns a dictionary
    cpu, ram, disk, uptime, temperature = metrics_data['cpu_usage'], metrics_data['ram_usage'], metrics_data['disk_usage'], metrics_data['uptime'], metrics_data.get('temperature')

    # Save metrics to the database
    current_metrics = SystemMetrics.objects.create(
        cpu_usage=cpu,
        ram_usage=ram,
        disk_usage=disk,
        uptime=uptime,
        temperature=temperature
    )

    # Fetch the latest 10 records for historical data
    historical_data = SystemMetrics.objects.all().order_by('-timestamp')[:10]

    return render(request, 'dashboard.html', {
        'current_metrics': current_metrics,
        'historical_data': historical_data
    })
def get_alerts(request):
    # Fetch thresholds
    threshold, _ = Threshold.objects.get_or_create(id=1)

    # Get current metrics
    metrics = get_system_metrics()

    # Check for alerts
    alerts = []
    if metrics['cpu_usage'] > threshold.cpu_usage_threshold:
        alerts.append(f"High CPU Usage: {metrics['cpu_usage']}% exceeds {threshold.cpu_usage_threshold}%")
    if metrics['ram_usage'] > threshold.ram_usage_threshold:
        alerts.append(f"High RAM Usage: {metrics['ram_usage']} GB exceeds {threshold.ram_usage_threshold} GB")
    if metrics['disk_usage'] < threshold.disk_usage_threshold:
        alerts.append(f"Low Disk Space: {metrics['disk_usage']} GB is below {threshold.disk_usage_threshold} GB")
    if metrics['uptime'] > threshold.uptime_threshold:
        alerts.append(f"High Uptime: {metrics['uptime']} hours exceeds {threshold.uptime_threshold} hours")
    if metrics['temperature'] and metrics['temperature'] > threshold.temperature_threshold:
        alerts.append(f"High Temperature: {metrics['temperature']}°C exceeds {threshold.temperature_threshold}°C")

    # Return alerts as JSON
    return JsonResponse({'alerts': alerts})


def update_threshold(request):
    if request.method == 'POST':
        threshold, _ = Threshold.objects.get_or_create(id=1)
        threshold.cpu_usage_threshold = request.POST.get('cpu_usage_threshold', threshold.cpu_usage_threshold)
        threshold.ram_usage_threshold = request.POST.get('ram_usage_threshold', threshold.ram_usage_threshold)
        threshold.disk_usage_threshold = request.POST.get('disk_usage_threshold', threshold.disk_usage_threshold)
        threshold.uptime_threshold = request.POST.get('uptime_threshold', threshold.uptime_threshold)
        threshold.temperature_threshold = request.POST.get('temperature_threshold', threshold.temperature_threshold)
        threshold.save()
    return redirect('dashboard')