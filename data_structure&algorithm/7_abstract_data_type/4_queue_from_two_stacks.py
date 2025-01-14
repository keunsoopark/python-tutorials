# Use two lists to achieve O(1)
# cf) in 3_queue, it was O(n) as using only one list
# This example is bullshit. Because it works when enqueue is used only once. After line 60, 10 is not in queue.
# (only in out_stack, but not in in_stack


class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("Queue is empty!")

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print("Queue is empty!")

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is empty!")

    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))


if __name__ == "__main__":
    queue = Queue()
    print(f"Queue is empty? {queue.isEmpty()}")
    print(f"Add numbers 0 - 9 in queue.")
    for i in range(10):
        queue.enqueue(i)
    print(f"Size of queue: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"Queue is empty? {queue.isEmpty()}")

    queue.enqueue(10)

    print(queue)
