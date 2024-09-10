import psutil


class Metrics:
    def __init__(self):
        pass

    @staticmethod
    def collect():
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        io_counters = psutil.disk_io_counters()
        network_info = psutil.net_if_stats()
        network_counters = psutil.net_io_counters(pernic=True)

        metrics = {
            'cpu_percent': cpu_percent,
            'memory': {
                'total': memory_info.total,
                'available': memory_info.available,
                'percent': memory_info.percent,
            },
            'disk': {
                'total': disk_usage.total,
                'used': disk_usage.used,
                'free': disk_usage.free,
                'percent': disk_usage.percent,
            },
            'io': {
                'read_count': io_counters.read_count,
                'write_count': io_counters.write_count,
                'read_bytes': io_counters.read_bytes,
                'write_bytes': io_counters.write_bytes,
            },
            'network': {
                nic: {
                    'is_up': network_info[nic].isup,
                    'speed': network_info[nic].speed,
                    'received_bytes': network_counters[nic].bytes_recv,
                    'sent_bytes': network_counters[nic].bytes_sent,
                    'received_packets': network_counters[nic].packets_recv,
                    'sent_packets': network_counters[nic].packets_sent,
                }
                for nic in network_info
            }
        }

        return metrics
