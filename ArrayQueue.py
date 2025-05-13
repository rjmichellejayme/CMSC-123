class Element:
    def __init__(self, value, index):
        self.value = value  # Store the value and index of the element.
        self.index = index  

    def setValue(self, value):
        self.value = value  # Set the value of the element.

    def getValue(self):
        return self.value  # Get the value of the element.

    def getIndex(self):
        return self.index  # Get the index of the element.

class Array:
    def __init__(self, capacity=10):
        self.contents = [None] * capacity  # Initialize an array with the given capacity.
        self.size = 0  # Initialize the size of the array to 0.
        self.capacity = capacity  # Store the maximum capacity of the array.
        self.DEFAULT_EXPANSION = 5  # Define a default expansion value for resizing.

    def getSize(self):
        return self.size  # Get the current size of the array.

    def getCapacity(self):
        return self.capacity  # Get the capacity of the array.

    def isEmpty(self):
        return self.size == 0  # Check if the array is empty.

    def expand(self):
        self.capacity += self.DEFAULT_EXPANSION  # Increase the capacity of the array.

class ArrayQueue(Array):
    def front(self):
        if self.isEmpty():
            return Element(None, None)  # Return an empty Element if the queue is empty.
        else:
            return self.contents[0]  # Return the first element in the queue.

    def enqueue(self, value):  # checks if the queue is full by comparing the current size with the capacity
        if self.size >= self.capacity: 
            self.expand()  # Expand the queue if it's full.
        element = Element(value, self.size)  # Create an Element with the given value and index.
        self.contents[self.size] = element  # Add the element to the contents array.
        self.size += 1  # Increase the size of the queue.

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue from an empty queue.")  # Raise an exception if the queue is empty.
        else:
            removed_element = self.front()  # retrieves the front element to be removed
            for i in range(0, self.size - 1):   # iterates over the elements in the contents array
                self.contents[i] = self.contents[i + 1]  # Shift elements to the left to remove the front element.
            self.size -= 1  # Decrease the size of the queue.
            return removed_element  # Return the removed element.

