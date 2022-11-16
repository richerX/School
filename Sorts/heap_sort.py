# ----------------------------------------------------------------------------------------------------
# Пирамидальная сортировка (Heapsort) | Average O(n*log(n)) | Best O(n*log(n)) --> O(n*log(n)) Worst |
# ----------------------------------------------------------------------------------------------------

class heap:
    def __init__(self):
        self.data = mas_input
        self.length = n

    def sift_up(self, i):
        while i > 0:
            if self.data[i] > self.data[(i - 1) // 2]:
                self.data[i], self.data[(i - 1) // 2] = self.data[(i - 1) // 2], self.data[i]
            else:
                break
            i = (i - 1) // 2
        return i + 1
    
    def sift_down(self, i):
        while i * 2 + 1 < self.length:            
            if i * 2 + 2 > self.length - 1 or self.data[i * 2 + 1] >= self.data[i * 2 + 2]:
                j = i * 2 + 1
            else:
                j = i * 2 + 2                  
            if self.data[i] < self.data[j]:
                self.data[i], self.data[j] = self.data[j], self.data[i]
            else:
                break            
            i = j
        return i + 1
    
    def heapify(self):
        for i in range(self.length - 1, -1, -1):
            self.sift_down(i)
        
    def change(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.data.pop()
        self.length -= 1
        
    def get(self):
        return self.data
