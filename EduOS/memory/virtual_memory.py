class VirtualMemoryManager:
    def __init__(self, total_frames):
        self.total_frames = total_frames
        self.frames = [None] * total_frames     # (pid, page)
        self.ref_bits = [0] * total_frames
        self.clock_hand = 0

        self.page_faults = 0

    def _replace_page(self, process, page):
        while True:
            if self.ref_bits[self.clock_hand] == 0:
                victim = self.frames[self.clock_hand]
                if victim:
                    victim_pid, victim_page = victim
                    process_map = self.process_tables[victim_pid]
                    del process_map[victim_page]

                self.frames[self.clock_hand] = (process.pcb.pid, page)
                self.ref_bits[self.clock_hand] = 1
                frame = self.clock_hand
                self.clock_hand = (self.clock_hand + 1) % self.total_frames
                return frame
            else:
                self.ref_bits[self.clock_hand] = 0
                self.clock_hand = (self.clock_hand + 1) % self.total_frames

    def attach_process_tables(self, process_tables):
        # pid -> page_table
        self.process_tables = process_tables

    def access(self, process, logical_address, page_size):
        page = logical_address // page_size
        offset = logical_address % page_size

        # Page hit
        if page in process.pcb.page_table:
            frame = process.pcb.page_table[page]
            self.ref_bits[frame] = 1
            return frame * page_size + offset, False

        # Page fault
        self.page_faults += 1

        # Try empty frame first
        for i in range(self.total_frames):
            if self.frames[i] is None:
                self.frames[i] = (process.pcb.pid, page)
                self.ref_bits[i] = 1
                process.pcb.page_table[page] = i
                return i * page_size + offset, True

        # Replace using clock algorithm
        frame = self._replace_page(process, page)
        process.pcb.page_table[page] = frame
        return frame * page_size + offset, True
