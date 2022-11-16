class Queue():
    def __init__(self):
        self.data = []
        self.head = 0
        self.length = 0
    
    def push(self, value):
        self.data.append(value)
        self.length += 1          

    def pop(self):
        result = self.data[self.head]
        self.data[self.head] = None
        self.head += 1
        self.length -= 1
        return result

    def front(self):
        return self.data[self.head]
    
    def size(self):
        return self.length
        
    def empty(self):
        return self.length == 0
    
    def clear(self):
        self.__init__()  
        
    def get(self):
        return self.data
