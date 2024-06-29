# FIFO, First In First Out, like a pipe

from collections import deque

class Queue():
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return "Queue is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
        
    def size(self):
        return len(self.queue)


