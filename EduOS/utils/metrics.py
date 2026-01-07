class Metrics:
    def __init__(self):
        self.waiting_times = []
        self.turnaround_times = []
        self.response_times = []
        self.completion_times = []

        self.page_faults = 0
        self.memory_accesses = 0

        self.cpu_busy_time = 0
        self.total_time = 0

    def record_process(self, process):
        turnaround = process.pcb.completion_time - process.pcb.arrival_time
        waiting = turnaround - process.pcb.burst_time

        self.turnaround_times.append(turnaround)
        self.waiting_times.append(waiting)

    def record_response(self, response_time):
        self.response_times.append(response_time)

    def record_cpu_tick(self):
        self.cpu_busy_time += 1

    def record_time(self):
        self.total_time += 1

    def record_page_access(self, fault=False):
        self.memory_accesses += 1
        if fault:
            self.page_faults += 1

    def summary(self):
        return {
            "avg_waiting_time": sum(self.waiting_times) / len(self.waiting_times),
            "avg_turnaround_time": sum(self.turnaround_times) / len(self.turnaround_times),
            "avg_response_time": sum(self.response_times) / len(self.response_times),
            "cpu_utilization": self.cpu_busy_time / self.total_time,
            "page_fault_rate": (
                self.page_faults / self.memory_accesses
                if self.memory_accesses else 0
            )
        }


def calculate_metrics(processes):
    """
    Calculate scheduling metrics for a list of processes
    
    Args:
        processes: List of Process objects
    
    Returns:
        dict: Dictionary containing average waiting time and turnaround time
    """
    if not processes:
        return {'avg_waiting_time': 0, 'avg_turnaround_time': 0}
    
    waiting_times = []
    turnaround_times = []
    
    for p in processes:
        if hasattr(p.pcb, 'completion_time') and hasattr(p.pcb, 'arrival_time'):
            turnaround = p.pcb.completion_time - p.pcb.arrival_time
            waiting = turnaround - p.pcb.burst_time
            waiting_times.append(max(0, waiting))
            turnaround_times.append(turnaround)
    
    avg_waiting = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    avg_turnaround = sum(turnaround_times) / len(turnaround_times) if turnaround_times else 0
    
    return {
        'avg_waiting_time': avg_waiting,
        'avg_turnaround_time': avg_turnaround
    }

