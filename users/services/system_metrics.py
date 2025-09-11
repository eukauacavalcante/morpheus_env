import psutil


def get_system_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_total = ram.total / (1024 ** 3)
    ram_used = ram.used / (1024 ** 3)
    memory = psutil.disk_usage('/')
    memory_used = memory.used / (1024 ** 3)
    memory_total = memory.total / (1024 ** 3)

    return {
        'cpu_percent': cpu_percent,
        'ram_percent' : ram_percent,
        'ram_total': round(ram_total, 2),
        'ram_used' : round(ram_used, 2),
        'memory_used': round(memory_used, 2),
        'memory_total': round(memory_total, 2)
    }
