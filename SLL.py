
class SLLNode:
    def __init__(self, value, nextNode=None):
        self.value = value      # Initialize the value of the node.
        self.nextNode = None   # Initialize a reference to the next node (default is None).

    def setValue(self, value):
        self.value = value  # Set a new value for the node.

    def getValue(self):
        return self.value  # Retrieve the current value of the node.

    def setNext(self, nextNode):
        self.nextNode = nextNode  # Set the reference to the next node.

    def getNext(self):
        return self.nextNode  # Retrieve the reference to the next node.

class SLL:
    def __init__(self):
        self.size = 0           # Initialize the size of the SLL that keeps track of the number of nodes in the linked list.
        self.first = SLLNode(None)  # Initialize the first and last node (with None as its value).
        self.last = SLLNode(None)  

    def isEmpty(self):
        return self.size == 0  # Check if the SLL is empty by comparing its size to 0.


    def addNode(self, value):
        new_node = SLLNode(value) # create new node with the desired value that will be stored inside

        if self.size == 0:
            self.first = new_node  # Set the new node as the first node

        if self.last is not None:
            self.last.nextNode = new_node  # Update the next node of the current last node to point to the new node

        self.last = new_node  # empty or not, updates the last node to be the newly added node 
        self.size += 1  # Increment the size of the SLL

        return new_node

    def removeNode(self, variable):
        if self.isEmpty():
            return  # Return if the SLL is empty, as there's nothing to remove.

        # Check if the first node contains the value to be removed.
        if self.first.getValue() == variable: # if first node is the same with the value that we're going to remove

            new_first = self.first.getNext() # creates a new variable, updates the first node to point to the next node (removing the first node)
            self.first.setNext(SLLNode(None))   
            self.first = new_first # new_first will be the first node 

            if self.size == 1:
                self.first = SLLNode(None)  # if the linked list has only 1 node then reset the first and last node with none value
                self.last = SLLNode(None)  
            self.size -= 1  # Decrement the size of the linked list.

            return

        # If the value is not in the first node, use a previous node to traverse and remove the node with the given value.
        prev = self.first
        current = self.first.getNext() # current = value of the node that comes after the first node (next node) that will make it the 2nd node of the list 

        while current is not None:

            if variable == current.getValue(): # found a node that needs to be removed
                prev.setNext(current.getNext())  # Update the previous node's next reference to point to the node that comes after current
                current.setNext(SLLNode(None))  # Clear references for the removed node by setting its next attribute to a new node with a value of None

                if current == self.last: # if the removed node was the last node
                    self.last = prev  # update the last node of the linked list to point to the prev node, effectively changing the last node reference
                self.size -= 1  # decrement the size of the SLL to reflect the removal of a node

                return
                
            prev = current # updates the prev pointer to point to the same node that current is currently pointing to
            current = current.getNext() # updates the current pointer to point to the next node in the linked list
