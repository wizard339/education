class Queue:

    def __init__(self, n=100):
        self.queue = [None] * n
        self.length = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def queue_empty(self):
        return self.size == 0

    def queue_full(self):
        return self.size == self.length
    
    def enqueue(self, x):
        if self.queue_full():
            print('The queue is full!')
            return
        self.queue[self.tail] = x
        self.tail += 1
        self.size += 1
        print(f'Added value: {x}')

    def dequeue(self):
        if self.queue_empty():
            print('The queue is empty!')
            return None
        x = self.queue[self.head]
        self.head += 1
        self.size -= 1
        print(f'Removed value: {x}')
        return x

    def peek(self):
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
