from utils.metrics import Metrics

def run_scheduler(kernel, scheduler_fn, processes):
    kernel.metrics = Metrics()
    gantt = scheduler_fn(processes)

    for p in processes:
        kernel.metrics.record_process(p)

    return kernel.metrics.summary(), gantt
