# EduOS – Educational Operating System Kernel Simulator

## Overview
EduOS is a policy-level operating system kernel simulator built to study and
experiment with core OS responsibilities such as CPU scheduling, virtual memory,
concurrency, and safety.

The project focuses on decision-making and trade-offs rather than hardware-
dependent kernel mechanisms.

## Motivation
Operating systems are often taught as isolated algorithms. EduOS was built to
integrate these concepts into a single system where scheduling, memory management,
and concurrency interact and can be measured objectively.

## Features
- Preemptive CPU scheduling (SRTF, Priority with Aging, MLFQ)
- Per-process virtual memory with page tables
- Clock (second-chance) page replacement
- Thread model with mutexes and semaphores
- System calls: fork, exec, wait, exit
- Deadlock handling concepts
- Performance metrics and visualization
- Policy comparison and fault injection

## Architecture
EduOS is organized into modular subsystems:
- Scheduler
- Memory Manager
- Process & Thread Manager
- Synchronization Primitives
- Metrics & Visualization

Each subsystem models OS policy decisions independently while interacting through
a central kernel abstraction.


## How to Run
```bash
git clone https://github.com/<your-username>/EduOS-Kernel-Simulator
cd EduOS-Kernel-Simulator
python main.py

## Academic Alignment
This project aligns with core Operating Systems topics:
- Process management and scheduling
- Virtual memory and page replacement
- Concurrency and synchronization
- Deadlocks and safety

## Limitations
- This is a simulator, not a real operating system
- Does not run on bare hardware
- Does not manage real memory or devices
- Focuses on policy modeling, not kernel mechanisms

## License
MIT License
