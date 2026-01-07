class SysCallHandler:
    def __init__(self, kernel):
        self.kernel = kernel
        self.next_pid = 100  # child PIDs start higher for clarity

    def fork(self, parent_proc):
        child_pid = self.next_pid
        self.next_pid += 1

        child = self.kernel.create_process(
            pid=child_pid,
            arrival_time=self.kernel.time,
            burst_time=parent_proc.pcb.remaining_time,
            priority=parent_proc.pcb.priority
        )

        # Parent-child relationship
        child.pcb.parent = parent_proc
        parent_proc.pcb.children.append(child)

        # Copy page table (logical copy, not physical duplication)
        child.pcb.page_table = parent_proc.pcb.page_table.copy()

        return child

    def exec(self, process, new_burst_time):
        # Replace program (simulate by resetting burst time)
        process.pcb.burst_time = new_burst_time
        process.pcb.remaining_time = new_burst_time

    def exit(self, process):
        process.pcb.state = "TERMINATED"
        process.pcb.completion_time = self.kernel.time

        # Wake parent if waiting
        parent = process.pcb.parent
        if parent and parent.pcb.state == "WAITING":
            parent.pcb.state = "READY"
            self.kernel.ready_queue.append(parent)

    def wait(self, process):
        # Block until all children terminate
        for child in process.pcb.children:
            if child.pcb.state != "TERMINATED":
                process.pcb.state = "WAITING"
                return
        # All children terminated