from process.process import Process

def standard_workload():
    return [
        Process(1, 0, 10),
        Process(2, 1, 3),
        Process(3, 2, 6),
        Process(4, 4, 4),
    ]
