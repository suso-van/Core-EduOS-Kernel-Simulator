def srtf(processes):
    time = 0
    completed = 0
    n = len(processes)

    processes = sorted(processes, key=lambda p: p.pcb.arrival_time)
    ready = []
    gantt = []
    last_pid = None

    while completed < n:
        # Add arrived processes
        for p in processes:
            if p.pcb.arrival_time == time:
                ready.append(p)

        # Choose process with shortest remaining time
        if ready:
            ready.sort(key=lambda p: p.pcb.remaining_time)
            current = ready[0]

            # Gantt tracking (context switch aware)
            if last_pid != current.pcb.pid:
                gantt.append((current.pcb.pid, time))
                last_pid = current.pcb.pid

            # Execute for 1 time unit
            current.pcb.remaining_time -= 1

            # Process completed
            if current.pcb.remaining_time == 0:
                completed += 1
                ready.remove(current)
                current.pcb.completion_time = time + 1

        time += 1

    # Close Gantt chart
    final_gantt = []
    for i in range(len(gantt)):
        pid, start = gantt[i]
        end = gantt[i + 1][1] if i + 1 < len(gantt) else time
        final_gantt.append((pid, start, end))

    return final_gantt
