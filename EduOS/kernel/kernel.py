"""
EduOS Kernel Module
Main kernel implementation for OS concepts
"""
from utils.metrics import Metrics
from kernel.syscalls import SysCallHandler


class Kernel:
    def __init__(self):
        self.ready_queue = []
        self.waiting_queue = []
        self.running_process = None
        self.time = 0
        self.process_table = {}
        self.metrics = Metrics()
        self.syscalls = SysCallHandler(self)

    def create_process(self, pid, arrival_time, burst_time, priority=5):
        """Create a new process"""
        from process.process import Process
        p = Process(pid, arrival_time, burst_time, priority)
        self.process_table[pid] = p
        p.pcb.state = "READY"
        self.ready_queue.append(p)
        return p

    def tick(self, cpu_active=True):
        """Increment kernel tick"""
        self.metrics.record_time()
        if cpu_active:
            self.metrics.record_cpu_tick()
        self.time += 1


