#!/usr/bin/env python

class Node(object):
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        current = self.head
        while current:
            print "Node({})".format(current.data),
            current = current.next

    def preppend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


if __name__ == "__main__":
    li = LinkedList()
    li.append(2)
    li.append(3)
    li.preppend(1)
    li.preppend(2)
    li.preppend(3)
    li.print_list()
