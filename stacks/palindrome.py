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


def is_palindrome(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    for i in xrange(len(s)):
        if s[i] != stack.pop():
            return False

    return True


if __name__ == "__main__":

    values = {
        "palindrome": [
            "abccba",
            "aba",
            "012345543210"
        ],
        "non_palindrome": [
            "abc",
            "home"
        ]
    }

    for value in values["palindrome"]:
        assert is_palindrome(value)

    for value in values["non_palindrome"]:
        assert not is_palindrome(value)
