class Thread:
    def __init__(self, tid, process):
        self.tid = tid
        self.process = process
        self.state = "READY"
