"""
Priority Scheduler
"""

def priority_scheduling(processes):
    time = 0
    ready = []
    gantt = []
    stats = []

    processes = sorted(processes, key=lambda x: x.pcb.arrival_time)

    while processes or ready:
        while processes and processes[0].pcb.arrival_time <= time:
            ready.append(processes.pop(0))

        if ready:
            ready.sort(key=lambda x: x.pcb.priority)
            p = ready.pop(0)

            start = time
            time += p.pcb.burst_time
            end = time

            waiting = start - p.pcb.arrival_time
            turnaround = end - p.pcb.arrival_time

            gantt.append((p.pcb.pid, start, end))
            stats.append((p.pcb.pid, waiting, turnaround))
        else:
            time += 1

    return gantt, stats
