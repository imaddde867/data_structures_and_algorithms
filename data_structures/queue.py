from collections import deque

class Queue:

    def __init__(self):
        """Initializes an empty queue."""
        self.items = deque()

    def is_empty(self):
        """Checks if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """Adds an item to the end of the queue.

        """
        self.items.append(item)

    def dequeue(self):
        """Removes and return the front item of the queue.

        Returns:
            The item at the front of the queue.

        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        return self.items.popleft()

    def peek(self):
        """Returns the front item w/o removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue.

        Returns:
            int: The size of the queue.
        """
        return len(self.items)

# Examples of using Queue with real data


if __name__ == "__main__":
    # Creates a queue instance
    queue = Queue()

    # Adds some items to the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue: 1, 2, 3:")
    print(list(queue.items)) 

    # Dequeue an item
    dequeued_item = queue.dequeue()
    print(f"Dequeued item: {dequeued_item}") 

    # Checks the front item
    front_item = queue.peek()
    print(f"Front item after dequeue: {front_item}")  

    # Checks the size of the queue
    queue_size = queue.size()
    print(f"Queue size: {queue_size}")  

    # Dequeues remaining items
    queue.dequeue()
    queue.dequeue()

    # Checks if the queue is empty
    is_empty = queue.is_empty()
    print(f"Is the queue empty? {is_empty}")  