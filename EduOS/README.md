# EduOS - Educational Operating System Simulator

An educational project implementing core operating system concepts including process management, scheduling, memory management, and deadlock avoidance.

## Project Structure

```
EduOS/
├── kernel/
│   └── kernel.py          # Main kernel implementation
├── process/
│   ├── process.py         # Process management
│   └── pcb.py            # Process Control Block
├── scheduler/
│   ├── fcfs.py           # First Come First Served
│   ├── sjf.py            # Shortest Job First
│   ├── priority.py       # Priority Scheduling
│   └── round_robin.py    # Round Robin Scheduling
├── memory/
│   ├── paging.py         # Virtual memory paging
│   └── page_replacement.py # Page replacement algorithms
├── deadlock/
│   └── bankers.py        # Banker's Algorithm
├── utils/
│   └── logger.py         # Logging utility
├── main.py               # Entry point
└── README.md            # This file
```

## Components

### Kernel
Core kernel functionality for system initialization and management.

### Process Management
- **Process**: Represents a process in the system
- **PCB**: Process Control Block storing process state and information

### Scheduling Algorithms
- **FCFS**: First Come First Served
- **SJF**: Shortest Job First
- **Priority**: Priority-based scheduling
- **Round Robin**: Time-based scheduling

### Memory Management
- **Paging**: Virtual memory implementation
- **Page Replacement**: Various page replacement strategies

### Deadlock Management
- **Banker's Algorithm**: Deadlock avoidance

### Utilities
- **Logger**: System-wide logging functionality

## Getting Started

```python
python main.py
```

## License

MIT License
