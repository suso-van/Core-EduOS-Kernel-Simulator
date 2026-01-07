"""
First Come First Served (FCFS) Scheduler
"""

def fcfs(processes):
    time = 0
    gantt = []
    stats = []

    for p in sorted(processes, key=lambda x: x.pcb.arrival_time):
        if time < p.pcb.arrival_time:
            time = p.pcb.arrival_time

        start = time
        time += p.pcb.burst_time
        end = time

        waiting = start - p.pcb.arrival_time
        turnaround = end - p.pcb.arrival_time

        gantt.append((p.pcb.pid, start, end))
        stats.append((p.pcb.pid, waiting, turnaround))

    return gantt, stats
