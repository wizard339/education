class Stack:

    def __init__(self):
        self.stack = []
        self.top = len(self.stack)

    def stack_empty(self):
        if self.top == 0: return True
        else: return False

    def push(self, x):
        self.top += 1
        self.stack.append(x)

    def pop(self):
        if self.stack_empty():
            raise 'underflow'
        else:
            self.top -= 1
            return self.stack.pop()

    def multipop(self, k):
        while self.stack_empty()==False and k > 0:
            self.pop()
            k -= 1


if __name__=='__main__':
    b = Stack()
    print(b.top)
    print(b.stack_empty())
    b.push(5)
    print(b.top)
    print(b.pop())
    print(b.top)
    b.push(5)
    b.push(5)
    print(b.top)
    b.multipop(3)
    print(b.top)
