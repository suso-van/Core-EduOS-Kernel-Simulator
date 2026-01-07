"""
EduOS - Educational Operating System Simulator
Main entry point demonstrating all OS concepts
"""

# ==================== IMPORTS ====================
from kernel.kernel import Kernel
from process.process import Process
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.priority import priority_scheduling
from scheduler.round_robin import round_robin
from scheduler.srtf import srtf
from scheduler.preemptive_priority import preemptive_priority
from memory.paging import PagingSystem
from memory.page_replacement import fifo, lru, optimal
from deadlock.bankers import is_safe
from utils.logger import Logger
from utils.metrics import calculate_metrics

# Import fault injection
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from experiments.fault import inject_cpu_delay, inject_page_fault, get_fault_injector

# ==================== INITIALIZATION ====================
logger = Logger("EduOS")


def print_header():
    """Print the main header"""
    print("=" * 60)
    print("EduOS - Educational Operating System Simulator")
    print("=" * 60)


def print_section(title):
    """Print section separator"""
    print(f"\n{title}")
    print("-" * 60)


# ==================== MAIN FUNCTIONS ====================
def demo_process_management():
    """Demonstrate process management"""
    print_section("[1] PROCESS MANAGEMENT")
    
    kernel = Kernel()
    
    # Create processes
    processes = [
        kernel.create_process(1, 0, 5),
        kernel.create_process(2, 1, 3),
        kernel.create_process(3, 2, 8),
        kernel.create_process(4, 3, 6)
    ]
    
    for p in processes:
        logger.info(f"Process {p.pcb.pid} created with burst time {p.pcb.burst_time}")
    
    print(f"Total processes created: {len(kernel.ready_queue)}")
    return processes, kernel


def demo_scheduling(processes):
    """Demonstrate CPU scheduling algorithms"""
    print_section("[2] CPU SCHEDULING ALGORITHMS")
    
    # FCFS Scheduling
    fcfs_gantt, fcfs_stats = fcfs(processes)
    print(f"FCFS Gantt Chart: {fcfs_gantt}")
    print(f"FCFS Statistics: {fcfs_stats}")
    
    # SJF Scheduling
    sjf_gantt, sjf_stats = sjf(processes)
    print(f"\nSJF Gantt Chart: {sjf_gantt}")
    print(f"SJF Statistics: {sjf_stats}")
    
    # Priority Scheduling
    priority_gantt, priority_stats = priority_scheduling(processes)
    print(f"\nPriority Gantt Chart: {priority_gantt}")
    print(f"Priority Statistics: {priority_stats}")
    
    # Round Robin Scheduling
    rr_gantt, rr_stats = round_robin(processes, quantum=4)
    print(f"\nRound Robin Gantt Chart: {rr_gantt}")


def demo_paging():
    """Demonstrate memory management - paging"""
    print_section("[3] MEMORY MANAGEMENT - PAGING")
    
    paging = PagingSystem(frames=4)
    virtual_addresses = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3]
    for addr in virtual_addresses:
        paging.access_page(addr)
    print(f"Total Page Faults: {paging.page_faults}")


def demo_page_replacement():
    """Demonstrate page replacement algorithms"""
    print_section("[4] PAGE REPLACEMENT ALGORITHMS")
    
    page_sequence = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    
    # FIFO Page Replacement
    fifo_faults = fifo(page_sequence, frames=3)
    print(f"FIFO Page Faults: {fifo_faults}")
    
    # LRU Page Replacement
    lru_faults = lru(page_sequence, frames=3)
    print(f"LRU Page Faults: {lru_faults}")
    
    # Optimal Page Replacement
    optimal_faults = optimal(page_sequence, frames=3)
    print(f"Optimal Page Faults: {optimal_faults}")


def demo_deadlock_avoidance():
    """Demonstrate deadlock avoidance - Banker's algorithm"""
    print_section("[5] DEADLOCK AVOIDANCE - BANKER'S ALGORITHM")
    
    process_names = ["P0", "P1", "P2", "P3", "P4"]
    available = [3, 3, 2]
    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    
    safe, sequence = is_safe(process_names, available, max_need, allocation)
    print(f"System is in Safe State: {safe}")
    if safe:
        print(f"Safe Sequence: {sequence}")


def demo_kernel_dispatch(kernel):
    """Demonstrate kernel status"""
    print_section("[6] KERNEL STATUS")
    
    if kernel.running_process:
        print(f"Running Process: PID={kernel.running_process.pcb.pid}, "
              f"State={kernel.running_process.pcb.state}")
    else:
        print(f"Ready Queue has {len(kernel.ready_queue)} processes")
        for p in kernel.ready_queue:
            print(f"  - Process {p.pcb.pid}: State={p.pcb.state}, Burst Time={p.pcb.burst_time}")


def demo_srtf():
    """Demonstrate Shortest Remaining Time First scheduling"""
    print_section("[7] SRTF (SHORTEST REMAINING TIME FIRST)")
    
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 2),
        Process(4, 3, 1)
    ]
    
    gantt = srtf(processes)
    metrics = calculate_metrics(processes)
    
    print("SRTF Gantt Chart:")
    for g in gantt:
        print(g)
    print("Metrics:", metrics)


def demo_preemptive_priority():
    """Demonstrate preemptive priority scheduling"""
    print_section("[8] PREEMPTIVE PRIORITY SCHEDULING")
    
    processes = [
        Process(1, 0, 7, priority=4),
        Process(2, 1, 4, priority=1),
        Process(3, 2, 6, priority=5),
        Process(4, 3, 3, priority=2),
    ]
    
    gantt = preemptive_priority(processes)
    metrics = calculate_metrics(processes)
    
    print("Preemptive Priority Gantt:")
    for g in gantt:
        print(g)
    print("Metrics:", metrics)


def demo_fault_injection_scheduler():
    """Demonstrate scheduler with fault injection"""
    print_section("[9] SCHEDULER WITH FAULT INJECTION (CPU DELAYS)")
    
    kernel = Kernel()
    processes = [
        kernel.create_process(1, 0, 8),
        kernel.create_process(2, 1, 5),
        kernel.create_process(3, 2, 6),
    ]
    
    print("Simulating execution with fault injection (20% CPU delay probability):")
    print(f"{'Time':<6} {'Event':<30} {'CPU Active':<12}")
    print("-" * 50)
    
    total_time = 0
    for _ in range(20):
        if inject_cpu_delay(probability=0.2):
            kernel.tick(cpu_active=False)
            print(f"{total_time:<6} CPU Delay Injected           {'NO':<12}")
        else:
            kernel.tick(cpu_active=True)
            print(f"{total_time:<6} Normal Execution             {'YES':<12}")
        total_time += 1
    
    fault_stats = get_fault_injector().get_fault_statistics()
    print(f"\nTotal Faults Injected - CPU Delays: {fault_stats['cpu_faults']}")


def demo_fault_injection_memory():
    """Demonstrate memory access with fault injection"""
    print_section("[10] MEMORY ACCESS WITH FAULT INJECTION (PAGE FAULTS)")
    
    paging = PagingSystem(frames=3)
    page_sequence = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3]
    
    print("Simulating page access with fault injection (30% page fault probability):")
    print(f"{'Page':<6} {'Injected Fault':<20} {'Total Faults':<15}")
    print("-" * 42)
    
    fault_count = 0
    for page in page_sequence:
        paging.access_page(page)
        
        if inject_page_fault(probability=0.3):
            fault_count += 1
            fault_status = "YES"
        else:
            fault_status = "NO"
        
        print(f"{page:<6} {fault_status:<20} {fault_count:<15}")
    
    print(f"\nPage Faults from Paging System: {paging.page_faults}")
    print(f"Injected Page Faults: {fault_count}")
    fault_stats = get_fault_injector().get_fault_statistics()
    print(f"Total Faults Injected - Page Faults: {fault_stats['page_faults']}")


def demo_stress_test():
    """Demonstrate system under stress with multiple fault types"""
    print_section("[11] STRESS TEST - MULTIPLE FAULT TYPES")
    
    kernel = Kernel()
    processes = [
        kernel.create_process(1, 0, 10),
        kernel.create_process(2, 1, 8),
        kernel.create_process(3, 2, 6),
        kernel.create_process(4, 3, 5),
    ]
    
    paging = PagingSystem(frames=4)
    page_sequence = [1, 2, 3, 4, 5, 1, 2, 6, 3, 4, 1, 5, 2, 7, 3, 8]
    
    cpu_stalls = 0
    page_faults_injected = 0
    
    print(f"{'Iteration':<12} {'CPU Stall':<15} {'Page Fault':<15} {'Status':<20}")
    print("-" * 62)
    
    for i in range(len(page_sequence)):
        page = page_sequence[i]
        paging.access_page(page)
        
        cpu_fault = inject_cpu_delay(probability=0.25)
        page_fault = inject_page_fault(probability=0.35)
        
        if cpu_fault:
            cpu_stalls += 1
            kernel.tick(cpu_active=False)
        else:
            kernel.tick(cpu_active=True)
        
        if page_fault:
            page_faults_injected += 1
        
        status = ""
        if cpu_fault and page_fault:
            status = "CPU + PAGE FAULT"
        elif cpu_fault:
            status = "CPU Stall"
        elif page_fault:
            status = "Page Fault"
        else:
            status = "Normal"
        
        print(f"{i:<12} {str(cpu_fault):<15} {str(page_fault):<15} {status:<20}")
    
    fault_stats = get_fault_injector().get_fault_statistics()
    print(f"\n{'Metric':<30} {'Count':<10}")
    print("-" * 40)
    print(f"{'CPU Stalls':<30} {cpu_stalls:<10}")
    print(f"{'Page Faults Injected':<30} {page_faults_injected:<10}")
    print(f"{'Page Faults (Paging System)':<30} {paging.page_faults:<10}")
    print(f"{'Kernel Time':<30} {kernel.time:<10}")


# ==================== MAIN EXECUTION ====================
def main():
    """Main entry point"""
    print_header()
    
    # Run all demonstrations
    processes, kernel = demo_process_management()
    demo_scheduling(processes)
    demo_paging()
    demo_page_replacement()
    demo_deadlock_avoidance()
    demo_kernel_dispatch(kernel)
    demo_srtf()
    demo_preemptive_priority()
    
    # Run fault injection demonstrations
    demo_fault_injection_scheduler()
    demo_fault_injection_memory()
    demo_stress_test()
    
    # Final message
    print("\n" + "=" * 60)
    print("EduOS Simulation Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
