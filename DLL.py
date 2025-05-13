
class DLLNode:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value      # Initialize the value of the node
        self.nextNode = nextNode  # Initialize a reference to the next and previous node (default is None)
        self.prevNode = prevNode 

    def setValue(self, value):
        self.value = value  # Set a new value for the node

    def getValue(self):
        return self.value  # Retrieve the current value of the node

    def setNext(self, nextNode):
        self.nextNode = nextNode  # Set the reference to the next node

    def getNext(self):
        return self.nextNode  # Retrieve the reference to the next node

    def setPrev(self, prevNode):
        self.prevNode = prevNode  # Set the reference to the previous node

    def getPrev(self):
        return self.prevNode  # Retrieve the reference to the previous node

class DLL:
    def __init__(self):
        self.size = 0           # Initialize the size of the DLL (number of nodes)
        self.first = DLLNode(None)  # Initialize the first and last node (with None as its value)
        self.last = DLLNode(None)   

    def isEmpty(self):
        return self.size == 0  # Check if the DLL is empty by comparing its size to 0

    def addNode(self, value):

        new_node = DLLNode(value)  # Create a new DLLNode instance with the given value
        
        if self.isEmpty():
            self.first = new_node  # If the list is empty, set the new node as both first and last node
            self.last = new_node
        else:
            new_node.setPrev(self.last)  # set the previous node of the new_node to be the current last node to create backward link from the new node to the current last node
            self.last.setNext(new_node)  # updates the next reference of the current last node to point to the new_node that creates forward link from the last node to the new node
            self.last = new_node        # new node becomes the new last node in the list
        self.size += 1  # Increment the size of the list to reflect the addition of a new node

    def removeNode(self, value): # It starts by iterating through the list, searching for a node with the given value
        current = self.first  # Start from the first node
        
        while current is not None:
            if current.getValue() == value: # checks whether the value stored in the current node is equal to the target value
                
                if current.getPrev() is None:  # Check if it's the first node, if current has no previous node it means it's the first node
                    self.first = current.getNext()  # updates the first node to point to the next node, effectively removing the first node
                else:
                    current.getPrev().setNext(current.getNext())  # updates the next attribute of the previous node to point to the next node after current, to remove current from the list

                
                if current.getNext() is None:  # Check if it's the last node, if current has no next node it means it's the last node
                    self.last = current.getPrev()  # updates the last attribute to point to the previous node, to remove the last node
                    current.setPrev(DLLNode(None))  # Clear references
    
                else:
                    current.getNext().setPrev(current.getPrev())  # updates the prev attribute of the next node to point to the previous node, to remove current from the list

                current.setNext(DLLNode(None))  # Clear references.
                current.setPrev(DLLNode(None))

                self.size -= 1  # Decrement the size of the DLL.

                if self.isEmpty():
                    self.first = DLLNode(None)  # If the DLL is empty, reset first and last nodes.
                    self.last = DLLNode(None)
  
                return
                
            current = current.getNext()  # Move to the next node.
