from __future__ import print_function


class StackQueue(object):
    """A Queue implemented with two stacks"""
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


class QueueStack(object):
    """A Stack implemented with two queues"""
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        if self.queue1:
            self.queue1.append(data)
        else:
            self.queue2.append(data)

    def pop(self):
        # q is non-empty queue; e is empty queue
        if self.queue1:
            q = self.queue1
            e = self.queue2
        else:
            q = self.queue2
            e = self.queue1
        while len(q) != 1:
            e.append(q.pop(0))
        return q.pop(0)


def test_stack_queue():
    sq = StackQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    sq.enqueue(3)
    print(sq.dequeue())
    print(sq.dequeue())
    sq.enqueue(4)
    sq.enqueue(5)
    print(sq.dequeue())
    sq.enqueue(6)
    print(sq.dequeue())


def test_queue_stack():
    qs = QueueStack()
    qs.push(1)
    qs.push(2)
    print(qs.pop())
    qs.push(3)
    print(qs.pop())
    print(qs.pop())


if __name__ == '__main__':
    test_queue_stack()
