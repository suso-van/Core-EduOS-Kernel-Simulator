"""
Memory Paging Module
Implements virtual memory paging
"""

class PagingSystem:
    def __init__(self, frames):
        self.frames = frames
        self.memory = []
        self.page_faults = 0

    def access_page(self, page):
        if page not in self.memory:
            self.page_faults += 1
            if len(self.memory) < self.frames:
                self.memory.append(page)
            else:
                return False  # Page fault, replacement needed
        return True