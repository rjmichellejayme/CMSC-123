class Element:
    def __init__(self, value, index=0):
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
        self.size = 0 
        self.capacity = capacity 
        self.contents = [None] * self.capacity 
        self.DEFAULT_EXPANSION = 5  
        self.frontIndex = 0  
        self.rearIndex = 0 

    def getSize(self):
        return self.size  

    def getCapacity(self):
        return self.capacity  

    def isEmpty(self):
        return self.size == 0 

    def expand(self):
        self.capacity += self.DEFAULT_EXPANSION  # Increase the capacity by the default expansion value
        self.contents += [None] * self.DEFAULT_EXPANSION  # Expand the array

    def wrapAround(self):
        new_contents = [None] * self.capacity  # Create a new list to handle wrap-around
        for i in range(self.capacity):
            # calculates the index for the element in the self.contents list that needs to be moved 
            new_contents[i] = self.contents[(self.frontIndex + i) % self.capacity]  #  ensuring that when it reaches the end of the array, it wraps around to the beginning
        self.contents = new_contents # element from original contents list at calculated index is copied to the corresponding position in the new_contents list
        self.frontIndex = 0  # Reset the front index
        self.rearIndex = self.size  # Update the rear index

class CircularQueue(Array):
    def front(self):
        if self.isEmpty():
            return Element(None)  # Return an empty element if the queue is empty
        else:
            return self.contents[self.frontIndex]  # Return the front element

    def enqueue(self, value):
        new_elem = Element(value, self.size)  # Create a new element with the given value and size
        if self.size == self.capacity:
            self.expand()  # Expand the circular queue if it's full, increase the capacity and update the contents list 
            self.wrapAround()  # Perform wrap-around if needed, reorder the elements to fill those empty spaces
            self.enqueue(value)  # Try enqueueing the value again
        else:
            self.contents[self.rearIndex] = new_elem  # Add the new element to the rear
            self.rearIndex = (self.rearIndex + 1) % self.capacity  # Update the rear index
            self.size += 1  # Increase the size of the circular queue

    def dequeue(self):
        if self.isEmpty():
            raise Exception  # Raise an exception if the queue is empty
        else:
            removed = self.contents[self.frontIndex]  # Get the element to be removed
            self.contents[self.frontIndex] = Element(None)  # Set the element at the front to None
            self.frontIndex = (self.frontIndex + 1) % self.capacity  # Update the front index
            self.size -= 1  # Decrease the size of the circular queue
            return removed  # Return the removed element
