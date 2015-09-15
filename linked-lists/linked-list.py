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
        print

    def prepend(self, data):
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

    def remove(self, data):
        current = self.head

        # is head the node we are looking for?
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        # lets look for the next node while having a reference
        # to the previous so we can unlink the next reference on prev
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                break
            else:
                current = current.next

if __name__ == "__main__":
    li = LinkedList()
    li.append(2)
    li.append(3)
    li.prepend(1)
    li.prepend(2)
    li.prepend(3)
    li.print_list()
    li.remove(3)
    li.print_list()
