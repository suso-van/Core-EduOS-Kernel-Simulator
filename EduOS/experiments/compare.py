from kernel.kernel import Kernel
from experiments.workload import standard_workload
from experiments.run_policy import run_scheduler

from scheduler.fcfs import fcfs
from scheduler.srtf import srtf
from scheduler.mlfq import mlfq

def compare():
    policies = {
        "FCFS": fcfs,
        "SRTF": srtf,
        "MLFQ": mlfq
    }

    results = {}

    for name, policy in policies.items():
        kernel = Kernel()
        processes = standard_workload()
        metrics, _ = run_scheduler(kernel, policy, processes)
        results[name] = metrics

    return results
