import platform

import psutil


def get_system_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_total = ram.total / (1024**3)
    ram_used = ram.used / (1024**3)
    disk_path = 'C://' if platform.system() == 'Windows' else '/'
    memory = psutil.disk_usage(disk_path)
    memory_used = memory.used / (1024**3)
    memory_total = memory.total / (1024**3)

    return {
        'cpu_percent': cpu_percent,
        'ram_percent': ram_percent,
        'ram_total': round(ram_total, 2),
        'ram_used': round(ram_used, 2),
        'memory_used': round(memory_used, 2),
        'memory_total': round(memory_total, 2),
    }


def sanitize_system_data(status):
    return {
        'cpu_level': 'high' if status['cpu_percent'] > 80 else 'normal',
        'ram_level': 'high' if status['ram_percent'] > 80 else 'normal',
    }
