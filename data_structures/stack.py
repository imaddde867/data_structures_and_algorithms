# data_structures/stack.py

class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            bool: True if stack is empty/ False if stack is empty.
        """
        return len(self.items) == 0

    def push(self, item):
        """Adds an item to the top of the stack.

        Arguments:
            item: The item to be added.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the item on top of the stack.

        Returns:
            The item at the top of the stack.
        """
       
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        """Returns the top item without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack.

        Returns:
            int: The size of the stack.
        """
        return len(self.items)

#Real data example

def reverse_string(input_string):
    """Reverse a string using a stack."""
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str


if __name__ == "__main__":


# Example 1: Reversing a string
    original_string = "Hello, World!"
    reversed_string = reverse_string(original_string)
    print("Original String:", original_string)
    print("Reversed String:", reversed_string)
    print()