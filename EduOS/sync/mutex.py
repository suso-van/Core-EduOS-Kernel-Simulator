class Mutex:
    def __init__(self):
        self.locked = False
        self.owner = None
        self.wait_queue = []

    def acquire(self, thread):
        if not self.locked:
            self.locked = True
            self.owner = thread
        else:
            thread.state = "WAITING"
            self.wait_queue.append(thread)

    def release(self):
        if self.wait_queue:
            next_thread = self.wait_queue.pop(0)
            next_thread.state = "READY"
            self.owner = next_thread
        else:
            self.locked = False
            self.owner = None
