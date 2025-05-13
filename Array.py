# Represents individual elements with a value and an index
class Element:
    def __init__(self, value, index):
        self.value = value  # Initialize the value and index of the element
        self.index = index  

    def setValue(self, value):
        self.value = value  # Set a new value for the element to allow modification

    def getValue(self):
        return self.value  # Retrieve and return the current value of the element that will be used to access

# Represents a collection of elements
class Array:
    def __init__(self):
        self.size = 0          # Initialize the size of the array to keep track of the number of elements in the array.
        self.contents = []     # Initialize an empty list to store the elements.

    def isEmpty(self):
        return self.size == 0  # Check if the array is empty by comparing its size to 0.

    def addElement(self, value):
        element = Element(value, self.size)  # Create a new Element instance with the given value and index.
        self.contents.append(element)        # Appending the new element to the array's contents list.
        self.size += 1                       # Increment the size of the array to reflect addition of new element.

    def removeElement(self, index):
        if 0 <= index < self.size:  # Check if the index is within valid bounds. if the index >= 0 and < current size of the array 
            removed_element = self.contents.pop(index)  # Remove the element at the specified index from the list using pop
            self.size -= 1  # Decrement the size of the array

            # Update the indices of the remaining elements
            for i in range(index, self.size):
                self.contents[i].index = i

            return removed_element  # Return the removed element
        else:
            raise IndexError("Index out of range")  # Raise an IndexError if the index is out of range.
