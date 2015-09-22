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


def matched(a, b):
    return a == '[' and b == ']' or \
           a == '{' and b == '}' or \
           a == '(' and b == ')'


if __name__ == "__main__":
    stack = Stack()
    exp = "["

    balanced = True
    for idx, token in enumerate(exp):
        if token in ["[", "{", "("]:
            stack.push(token)
        elif token in ["]", "}", ")"]:
            if not matched(stack.pop(), token):
                balanced = False
                break
        else:
            print "Invalid token {}".format(token)
            balanced = False

    if stack.size() > 0:
        balanced = False

    print "Is '{}' balanced? {}".format(exp, balanced)
