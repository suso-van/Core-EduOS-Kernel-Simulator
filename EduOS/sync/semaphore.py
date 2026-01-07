class Semaphore:
    def __init__(self, value):
        self.value = value
        self.wait_queue = []

    def wait(self, thread):
        self.value -= 1
        if self.value < 0:
            thread.state = "WAITING"
            self.wait_queue.append(thread)

    def signal(self):
        self.value += 1
        if self.wait_queue:
            thread = self.wait_queue.pop(0)
            thread.state = "READY"
