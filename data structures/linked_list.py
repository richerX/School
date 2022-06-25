class LinkedListNode:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"{self.prev.value} <-> {self.value} <-> {self.next.value}"


class LinkedList:
    def __init__(self):
        self.data = []
        self.length = 0
    
    def __str__(self):
        result = ""
        for node in self.data:
            result += str(node.value) + " <-> "
        return result[:-5]
    
    def append(self, value):
        new_node = LinkedListNode(value, None, None)
        self.data.append(new_node)
        if self.length >= 1:
            self.data[-2].next = self.data[-1]
            self.data[-1].prev = self.data[-2]
        self.length += 1
    
    def empty(self):
        return self.length == 0
    
    def clear(self):
        self.__init__()
    
    def get(self):
        return self.data
