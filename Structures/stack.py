class Stack():
    def __init__(self):
        self.data = []
        self.length = 0

    def empty(self):
        return self.length == 0
    
    def push(self, value):
        self.data.append(value)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.data.pop()

    def back(self):
        return self.data[-1]

    def size(self):
        return self.length

    def clear(self):
        self.__init__()
        
    def get(self):
        return self.data
