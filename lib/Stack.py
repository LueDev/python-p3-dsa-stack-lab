class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if len(self.items) < 1 else False
        
    def push(self, item):
        if len(self.items) < self.limit: 
            self.items.append(item)
        else: 
            Exception("Stack overflow")

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else: 
            return None

    def peek(self):
        if len(self.items) != 0: 
            return self.items[len(self.items) - 1]
        else: 
            raise Exception("There are no items in the stack")
    
    def size(self):
        return len(self.items) if len(self.items) != 0 else 0

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items: 
            return len(self.items) - self.items.index(target) - 1
        else: 
            return -1
