"""
Process Control Block (PCB)
Stores process state and information
"""

class PCB:
    def __init__(self, pid, arrival_time, burst_time, priority=5):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

        self.priority = priority
        self.queue_level = 0
        self.wait_time = 0
        self.completion_time = None
        self.state = "NEW"

        self.parent = None
        self.children = []
        self.page_table = {}

