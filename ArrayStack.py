class Element:
    def __init__(self, value, index):
        self.value = value 
        self.index = index 

    def setValue(self, value):
        self.value = value  

    def getValue(self):
        return self.value  

    def getIndex(self):
        return self.index  

class Array:
    def __init__(self, capacity=10):
        self.contents = [None] * capacity 
        self.size = 0 
        self.capacity = capacity 
        self.DEFAULT_EXPANSION = 5  # Default expansion size when resizing the array

    def getCapacity(self):
        return self.capacity  

    def isEmpty(self):
        return self.size == 0  # Check if the array is empty by comparing size to 0

    def expand(self):
        self.capacity += self.DEFAULT_EXPANSION  # Increase the maximum capacity by the default expansion size
        new_contents = [None] * self.capacity  # Create a new array with the updated capacity
        for i in range(self.size):
            new_contents[i] = self.contents[i]  # Copy elements from the old array to the new one when the array is full
        self.contents = new_contents  # Update the array to the new expanded array

class ArrayStack(Array):

    def top(self):
        if self.isEmpty(): # It checks if the stack is empty before attempting to access the top element.
            return None  
        return self.contents[self.size - 1]  

    def push(self, value):
        if self.size < self.capacity:   # It checks if there is enough space in the array
            self.contents[self.size] = Element(value, self.size)  # Add an element with a value to the stack
            self.size += 1  # Increase the size of the stack
        else:
            raise Exception("Stack is full")  

    def pop(self):
        if self.isEmpty():
            raise Exception("pop() still working even if array is empty")  # Raise an exception if popping from an empty stack
        popped_element = self.contents[self.size - 1]  # Get the top element of the stack
        self.contents[self.size - 1] = None  # Clear the element from the array
        self.size -= 1  # Decrease the size of the stack
        return popped_element  # Return the popped element
