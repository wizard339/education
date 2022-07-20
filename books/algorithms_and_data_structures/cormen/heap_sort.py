class Heapsort:

    def __init__(self):
        self.arr = []
        self.heapsize = 0

    def parent(self, i):
        return i // 2
        
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heapsize and self.arr[l] > self.arr[i]:
            largest = l
        else:
            largest = i
        if r <= self.heapsize and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            # explicit exchange of values
            tmp = self.arr[largest]
            self.arr[largest] = self.arr[i]
            self.arr[i] = tmp
            self.heapify(largest)
       
    def build_heap(self, arr):
        self.heapsize = len(arr) - 1
        self.arr = arr
        for i in range((len(arr) // 2), -1, -1):
            self.heapify(i)
      
    def heapsort(self, arr):
        self.build_heap(arr)
        for i in range(len(arr) - 1, 0, -1):
            tmp = self.arr[0]
            self.arr[0] = self.arr[i]
            self.arr[i] = tmp
            self.heapsize -= 1
            self.heapify(0)
            

if __name__ == '__main__':
    a = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    h_sort = Heapsort()
    h_sort.build_heap(a)
    print(a)
    h_sort.heapsort(a)
    print(a)   
