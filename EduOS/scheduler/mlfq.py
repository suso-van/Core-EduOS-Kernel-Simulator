from collections import deque

Q0_QUANTUM = 2
Q1_QUANTUM = 4
AGING_LIMIT = 6

def mlfq(processes):
    time = 0
    completed = 0
    n = len(processes)

    processes = sorted(processes, key=lambda p: p.pcb.arrival_time)

    q0 = deque()
    q1 = deque()
    q2 = deque()

    gantt = []
    last_pid = None

    while completed < n:
        # Add arriving processes to highest queue
        for p in processes:
            if p.pcb.arrival_time == time:
                p.pcb.queue_level = 0
                q0.append(p)

        # Aging: promote waiting processes
        for q in [q1, q2]:
            for p in list(q):
                p.pcb.wait_time += 1
                if p.pcb.wait_time >= AGING_LIMIT:
                    q.remove(p)
                    p.pcb.queue_level = 0
                    p.pcb.wait_time = 0
                    q0.append(p)

        # Select queue
        if q0:
            current = q0.popleft()
            quantum = Q0_QUANTUM
        elif q1:
            current = q1.popleft()
            quantum = Q1_QUANTUM
        elif q2:
            current = q2.popleft()
            quantum = current.pcb.remaining_time
        else:
            time += 1
            continue

        # Gantt tracking
        if last_pid != current.pcb.pid:
            gantt.append((current.pcb.pid, time))
            last_pid = current.pcb.pid

        # Execute
        exec_time = min(quantum, current.pcb.remaining_time)
        current.pcb.remaining_time -= exec_time
        time += exec_time

        # Add new arrivals during execution
        for p in processes:
            if p.pcb.arrival_time > time - exec_time and p.pcb.arrival_time <= time:
                q0.append(p)

        # Process finished
        if current.pcb.remaining_time == 0:
            current.pcb.completion_time = time
            completed += 1
        else:
            # Demote process
            if current.pcb.queue_level == 0:
                current.pcb.queue_level = 1
                q1.append(current)
            elif current.pcb.queue_level == 1:
                current.pcb.queue_level = 2
                q2.append(current)
            else:
                q2.append(current)

    # Close Gantt chart
    final_gantt = []
    for i in range(len(gantt)):
        pid, start = gantt[i]
        end = gantt[i + 1][1] if i + 1 < len(gantt) else time
        final_gantt.append((pid, start, end))

    return final_gantt
