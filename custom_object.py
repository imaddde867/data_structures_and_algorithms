# custom_object.py

class CustomObject:
    """A simple custom object class for testing."""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"CustomObject({self.value})"

    def __eq__(self, other):
        if isinstance(other, CustomObject):
            return self.value == other.value
        return False
