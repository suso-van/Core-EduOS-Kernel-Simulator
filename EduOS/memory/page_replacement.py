"""
Page Replacement Algorithms
Implements various page replacement strategies
"""

def fifo(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
    return faults


def lru(pages, frames):
    memory = []
    recent = {}
    faults = 0

    for time, page in enumerate(pages):
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(recent, key=recent.get)
                memory.remove(lru_page)
                del recent[lru_page]
                memory.append(page)
        recent[page] = time
    return faults


def optimal(pages, frames):
    memory = []
    faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                future = pages[i+1:]
                index = {}
                for m in memory:
                    index[m] = future.index(m) if m in future else float('inf')
                victim = max(index, key=index.get)
                memory.remove(victim)
                memory.append(page)
    return faults

