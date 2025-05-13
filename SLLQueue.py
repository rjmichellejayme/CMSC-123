class SLLNode:
    def __init__(self, value):
        self.value = value  # Initialize the node with a value.
        self.nextNode = None  # Initialize the next node reference as None.

    def setValue(self, value):
        self.value = value  # Set the value of the node.

    def getValue(self):
        return self.value  # Get the value of the node.

    def setNext(self, nextNode):
        self.nextNode = nextNode  # Set the reference to the next node.

    def getNext(self):
        return self.nextNode  # Get the reference to the next node.

class SLL:
    def __init__(self):
        # Initialize an empty list with a size of 0 and no top node.
        self.size = 0
        self.frontNode = SLLNode(None)  # Initialize the front node with None value.
        self.frontNode.setNext(SLLNode(None))  # Initialize the next node reference as None.

    def getSize(self):
        return self.size  # Get the current size of the list.

    def isEmpty(self):
        # Check if the list is empty.
        return self.size == 0

class SLLQueue(SLL):
    
    def front(self):
        if self.isEmpty():
            return SLLNode(None)  # Return an empty node if the queue is empty.
        else:
            return self.frontNode  # Return the front node of the queue.
            
    def enqueue(self, value):
        new_node = SLLNode(value)  # Create a new node with the given value.
        current_node = self.frontNode

        if self.isEmpty():
            self.frontNode = new_node  # If the queue is empty, set the new node as the front node.
        else:
            while current_node.getNext() is not None:
                current_node = current_node.getNext()  # Traverse to the end of the queue.
            current_node.setNext(new_node)  # Set the new node as the next node of the last node.
    
        self.size += 1  # Increase the size of the queue.

    def dequeue(self):
        removed_element = self.frontNode  # Get the front node as the element to be removed.

        if self.isEmpty():
            raise Exception("dequeue() still working even if the array is empty")  # Raise an exception if the queue is empty.
        else:
            if self.frontNode.getNext is None:
                self.frontNode = SLLNode(None)  # If there's only one element, set the front node as an empty node.
            else:
                self.frontNode = self.frontNode.getNext()  # Move the front node to the next node.
                removed_element.setNext(None)  # Remove the reference to the next node from the removed element.
            self.size -= 1  # Decrease the size of the queue.
            return removed_element  # Return the removed element.

