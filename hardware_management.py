import psutil

class HardwareManager:
    def __init__(self):
        pass

    def get_cpu_info(self):
        return {
            "cpu_count": psutil.cpu_count(),
            "cpu_freq": psutil.cpu_freq().current,
            "cpu_percent": psutil.cpu_percent(interval=1)
        }

    def get_memory_info(self):
        memory = psutil.virtual_memory()
        return {
            "total_memory": memory.total,
            "available_memory": memory.available,
            "used_memory": memory.used,
            "memory_percent": memory.percent
        }

    def get_disk_usage(self, path="/"):
        disk_usage = psutil.disk_usage(path)
        return {
            "total_space": disk_usage.total,
            "used_space": disk_usage.used,
            "free_space": disk_usage.free,
            "disk_percent": disk_usage.percent
        }

# Example usage
if __name__ == "__main__":
    manager = HardwareManager()
    print("CPU Info:", manager.get_cpu_info())
    print("Memory Info:", manager.get_memory_info())
    print("Disk Usage:", manager.get_disk_usage("/"))
