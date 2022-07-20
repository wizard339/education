class BinHeap:

    def __init__(self):
        self.arr = []
        self.heapsize = 0

    def parent(self, i):
        """index of the parent value in the heap"""
        return i // 2
        
    def left(self, i):
        """index of the left descedent value in the heap"""
        return 2*i + 1
    
    def right(self, i):
        """index of the right descedent value in the heap"""
        return 2*i + 2
    
    def heapify(self, i):
        """the main property of the heap"""
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
            tmp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = tmp
            self.heapify(largest)
       
    def build_heap(self, arr):
        self.heapsize = len(arr) - 1
        self.arr = arr
        for i in range((len(arr) // 2), -1, -1):
            self.heapify(i)

    def build_heap_insert(self, arr):
        """building the heap with insertions"""
        self.heapsize = 1
        for i in range(1, len(arr)):
            self.heap_insert(self.arr, arr[i])
            
    def heapsort(self, arr):
        self.build_heap(arr)
        for i in range(len(arr) - 1, 0, -1):
            tmp = self.arr[0]
            self.arr[0] = self.arr[i]
            self.arr[i] = tmp
            self.heapsize -= 1
            self.heapify(0)

    def heap_extract_max(self, arr):
        """extraction of the max value from the heap"""
        self.build_heap(arr)
        if self.heapsize < 1:
            return 'the queue is empty'
        max_v = self.arr[0]
        self.arr[0] = self.arr[self.heapsize]
        self.arr.pop(self.heapsize)
        self.heapsize -= 1
        self.heapify(0)
        return max_v

    def heap_insert(self, arr, key):
        """insertion of the value to the heap"""
        # self.build_heap(arr)
        self.heapsize += 1
        i = self.heapsize - 1
        while i > 0 and self.arr[self.parent(i)] < key:
            self.arr[i] = self.arr[self.parent(i)]
            i = self.parent(i)
        self.arr[i] = key

    def heap_increase_key(self, arr, i, key):
        """
        increasing an element with index `i` to a value `k`
        """
        self.build_heap(arr)
        if self.arr[i] >= key:
            return
        else:
            while i > 0 and self.arr[self.parent(i)] < key:
                self.arr[i] = self.arr[self.parent(i)]
                i = self.parent(i)
            self.arr[i] = key

    def heap_delete(self, arr, i):
        """
        deleting an element with index `i` from the heap
        """
        arr.pop(i)
        self.build_heap(arr)


if __name__ == '__main__':
    a = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    b = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    print(f"Initial a: {a}")
    print(f"Initial b: {b}")
    
    heap = BinHeap()
    heap.build_heap(a)
    print(f"After using build_heap(a): {a}")
    heap.build_heap_insert(b)
    print(f"After using build_heap_insert(b): {b}")
    
    heap.heapsort(a)
    heap.heapsort(b)
    print(f"After sorting a: {a}")
    print(f"After sorting b: {b}")
    extracted_max = heap.heap_extract_max(a)
    print(f"Extracted max value: {extracted_max}")
    print(f"After exctracting of the max value: {a}")
    heap.heap_insert(a, 100)
    print(f"After insertion of the element: {a}")
    heap.heap_increase_key(a, 5, 50)
    print(f"After increasing of the element to value: {a}")
    heap.heap_delete(a, 0)
    print(f"After deleting of the element: {a}")
    
