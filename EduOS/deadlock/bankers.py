"""
Banker's Algorithm
Deadlock avoidance algorithm
"""

def is_safe(processes, available, max_need, allocation):
    n = len(processes)
    m = len(available)

    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    found = True
        if not found:
            return False, []

    return True, safe_sequence
