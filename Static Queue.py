class StaticQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    def enqueue(self, item):
        if self.is_full():
             print("Queue is full. Cannot enqueue.")
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.size += 1
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return item
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        else:
            return self.queue[self.front]
if __name__ == "__main__":
    queue = StaticQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("Queue: ", queue.queue)
    print("Dequeue:", queue.dequeue())
    print("Queue after dequeue: ", queue.queue)
    print("Peek:", queue.peek())
    print("Queue size:", queue.size)
    print("Is the queue empty?", queue.is_empty())
    print("Is the queue full?", queue.is_full())