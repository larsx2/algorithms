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
    stack = Stack()
    stack.push("(")
    stack.push(")")

    print "Poped:", stack.pop()
    print "Size:", stack.size()
    print "Peeked:", stack.peek()

