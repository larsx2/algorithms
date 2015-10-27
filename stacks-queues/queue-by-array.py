class Queue(object):
    def __init__(self):
        """ Queue ADT """
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.empty():
            return self.queue.pop()
        else:
            print "[WARNING] Empty Queue"

    def empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    # Operations:
    # * enqueue(): Add item to the queue
    # * dequeue(): Remove oldest item
    # * empty(): Is queue empty?
    # * size(): Size of the queue

    q = Queue()
    print "Is queue empty?", q.empty()

    for n in xrange(1, 4):
        print "[+] Adding {}".format(n)
        q.enqueue(n)
    print

    print "Queue size:", q.size()

    while not q.empty():
        print "[-] Dequeued:", q.dequeue()
    print

    if q.empty():
        print "Now queue is empty:", q.size()


