class Queue:
    def __init__(self, n=100):
        self.queue = [None] * n
        self.length = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def queue_empty(self):
        """method for checking for emptiness of the queue"""
        return self.size == 0

    def queue_full(self):
        """method for checking the completeness of the queue"""
        return self.size == self.length
    
    def enqueue(self, x):
        """method of inserting an item into the queue"""
        if self.queue_full():
            print('The queue is full!')
            return
        self.queue[self.tail] = x
        self.tail += 1
        self.size += 1
        print(f'Added value: {x}')

    def dequeue(self):
        """method of removing an item from the queue"""
        if self.queue_empty():
            print('The queue is empty!')
            return None
        x = self.queue[self.head]
        self.head += 1
        self.size -= 1
        print(f'Removed value: {x}')
        return x

    def peek(self):
        """method of getting the first item from the queue without deleting it"""
        if self.queue_empty():
            print('The queue is empty!')
            return
        return self.queue[self.head]


if __name__=='__main__':
    b = Queue(5)
    b.enqueue(1)
    b.enqueue(2)
    print(b.peek())
    print(b.dequeue())
    print(b.peek())
