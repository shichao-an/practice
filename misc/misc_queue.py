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


if __name__ == '__main__':

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
