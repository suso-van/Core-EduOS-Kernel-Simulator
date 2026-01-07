"""
Process Module
Handles process management and operations
"""
from thread.thread import Thread

class Process:
    def __init__(self, pid, arrival, burst, priority=5):
        from process.pcb import PCB
        self.pcb = PCB(pid, arrival, burst, priority)
        self.threads = []
        self.next_tid = 0

    def create_thread(self):
        t = Thread(self.next_tid, self)
        self.next_tid += 1
        self.threads.append(t)
        return t
