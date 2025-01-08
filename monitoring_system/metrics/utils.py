# metrics/utils.py
import psutil
import time
def collect_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().used / (1024 ** 3)  # Convert to GB
    disk_usage = psutil.disk_usage('/').used / (1024 ** 3)  # Convert to GB
    uptime = psutil.boot_time()
    temperature = None

    try:
        temperature = psutil.sensors_temperatures()['cpu_thermal'][0].current  # Optional, depending on the system
    except Exception as e:
        temperature = None

    return cpu_usage, ram_usage, disk_usage, uptime, temperature
def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().used / (1024 ** 3)  # Convert to GB
    disk_usage = psutil.disk_usage('/').used / (1024 ** 3)  # Convert to GB
    uptime = time.time() - psutil.boot_time()  # Convert to hours
    uptime_in_hours = uptime / 3600
    temperature = None  # Implement if available on your system
    return {
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'disk_usage': disk_usage,
        'uptime': uptime_in_hours,
        'temperature': temperature,
    }