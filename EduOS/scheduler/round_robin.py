"""
Round Robin Scheduler
"""

from collections import deque

def round_robin(processes, quantum):
    time = 0
    queue = deque()
    gantt = []
    stats = {}
    processes = sorted(processes, key=lambda x: x.pcb.arrival_time)

    while processes or queue:
        while processes and processes[0].pcb.arrival_time <= time:
            queue.append(processes.pop(0))

        if queue:
            p = queue.popleft()
            exec_time = min(quantum, p.pcb.remaining_time)

            start = time
            time += exec_time
            p.pcb.remaining_time -= exec_time
            end = time

            gantt.append((p.pcb.pid, start, end))

            while processes and processes[0].pcb.arrival_time <= time:
                queue.append(processes.pop(0))

            if p.pcb.remaining_time > 0:
                queue.append(p)
            else:
                turnaround = end - p.pcb.arrival_time
                waiting = turnaround - p.pcb.burst_time
                stats[p.pcb.pid] = (waiting, turnaround)
        else:
            time += 1

    return gantt, stats

