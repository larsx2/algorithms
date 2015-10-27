class Stack(object):
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return None

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    n = 22

    stack = Stack()
    while n:
        stack.push(n % 2)
        n /= 2

    print ''.join([
        str(stack.pop())
        for _ in range(0, stack.size())])

