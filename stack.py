from collections import deque
class Stack():
    def __init__(self) -> None:
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
        
    def size(self):
        return len(self.stack)