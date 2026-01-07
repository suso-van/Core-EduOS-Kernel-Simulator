AGING_INTERVAL = 3
MIN_PRIORITY = 0

def preemptive_priority(processes):
    time = 0
    completed = 0
    n = len(processes)

    processes = sorted(processes, key=lambda p: p.pcb.arrival_time)
    ready = []
    gantt = []
    last_pid = None

    while completed < n:
        # Add arriving processes
        for p in processes:
            if p.pcb.arrival_time == time:
                ready.append(p)

        # Apply aging to waiting processes
        for p in ready:
            p.pcb.wait_time += 1
            if p.pcb.wait_time % AGING_INTERVAL == 0:
                p.pcb.priority = max(MIN_PRIORITY, p.pcb.priority - 1)

        if ready:
            # Highest priority first
            ready.sort(key=lambda p: (p.pcb.priority, p.pcb.remaining_time))
            current = ready[0]

            # Gantt tracking
            if last_pid != current.pcb.pid:
                gantt.append((current.pcb.pid, time))
                last_pid = current.pcb.pid

            # Execute for 1 unit
            current.pcb.remaining_time -= 1

            if current.pcb.remaining_time == 0:
                current.pcb.completion_time = time + 1
                ready.remove(current)
                completed += 1

        time += 1

    # Close Gantt chart
    final_gantt = []
    for i in range(len(gantt)):
        pid, start = gantt[i]
        end = gantt[i + 1][1] if i + 1 < len(gantt) else time
        final_gantt.append((pid, start, end))

    return final_gantt
