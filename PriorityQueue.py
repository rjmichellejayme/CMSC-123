class Entry:
    def __init__(self, key, value):
        # Constructor for Entry class
        self.key = key
        self.value = value

    def setKey(self, key):
        # Set the key of the entry
        self.key = key

    def getKey(self):
        # Get the key of the entry
        return self.key

    def setValue(self, value):
        # Set the value of the entry
        self.value = value

    def getValue(self):
        # Get the value of the entry
        return self.value

class DLLNode:
    def __init__(self, entry, nextNode=None, prevNode=None):
        # Constructor for DLLNode class 
        self.entry = entry
        self.nextNode = nextNode
        self.prevNode = prevNode

    def setEntry(self, value):
        # Set the entry of the node
        self.entry = value

    def getEntry(self):
        # Get the entry of the node
        return self.entry

    def setNext(self, nextNode):
        # Set the next node
        self.nextNode = nextNode

    def getNext(self):
        # Get the next node
        return self.nextNode

    def setPrev(self, prevNode):
        # Set the previous node
        self.prevNode = prevNode

    def getPrev(self):
        # Get the previous node
        return self.prevNode

class UnsortedPQ():
    def __init__(self):
        # Constructor for UnsortedPQ class
        self.size = 0
        # Using a sentinel node to simplify edge cases with a default Entry (with None key and value) and uses it as both the head and tail
        self.headNode = self.tailNode = DLLNode(Entry(None, None))

    def getSize(self):
        # Get the size of the priority queue
        return self.size

    def isEmpty(self):
        # Check if the priority queue is empty
        return self.size == 0

    def find_min(self):
        # Find the node with the minimum key in the priority queue
        if self.isEmpty():
            raise IndexError("Priority queue is empty")
        else:
            # Initialize a pointer to the head of the priority queue
            current = self.headNode
            # Initialize variables to keep track of the node with the minimum key
            minNode = self.headNode
            minimum = minNode.getEntry()
            
            # Traverse the priority queue to find the node with the minimum key
            while current is not None:
                # Compare the key of the current node's entry with the minimum key
                if current.getEntry().getKey() < minimum.getKey():
                    # Update minNode and minimum if the current node has a smaller key to the current node and its key
                    minNode = current
                    minimum = current.getEntry()
                
                # Move to the next node in the priority queue
                current = current.getNext()
            
            # Return the node with the minimum key
            return minNode


    def insert(self, entry):
        # Insert an entry into the priority queue
        
        # Create a new node with the given entry
        newNode = DLLNode(entry)

        if self.isEmpty():
            # If the queue is empty, set both head and tail to the new node
            self.headNode = self.tailNode = newNode
        else:
            # Traverse the queue to find the insertion point
            
            # Start traversal from the head of the queue
            current = self.headNode
            
            # Check if the key already exists; if so, update the value and return
            while current is not None:
                # Compare the key of the current node's entry with the entry key
                if current.getEntry().getKey() == entry.getKey():
                    # Update the value of the existing entry and return
                    current.setEntry(entry)
                    return
                current = current.getNext()

            # If the key does not exist, insert at the end of the queue
            
            # Set the previous node of the new node to the current tail
            newNode.setPrev(self.tailNode)
            
            # Set the next node of the current tail to the new node
            self.tailNode.setNext(newNode)
            
            # Update the tail to be the new node
            self.tailNode = newNode

        # Increase the size of the priority queue
        self.size += 1


    def remove_min(self):
        # Remove the entry with the minimum key from the priority queue
        if self.isEmpty():
            raise IndexError("Priority queue is empty")
        else:
            # Find the node with the minimum key in the priority queue
            minimum = self.find_min()
        
            # Get references to the previous and next nodes of the minimum node
            prevNode = minimum.getPrev()
            nextNode = minimum.getNext()

            # Update headNode and tailNode if the minimum node is the head or tail
            if minimum == self.headNode:
                self.headNode = nextNode

            if minimum == self.tailNode:
                self.tailNode = prevNode

            # Update pointers of the previous and next nodes
            if prevNode is not None:
                prevNode.setNext(nextNode)

            if nextNode is not None:
                nextNode.setPrev(prevNode)

            # Disconnect the minimum node from the list
            minimum.setPrev(None)
            minimum.setNext(None)

            # Decrease the size of the priority queue
            self.size -= 1

            # Return the entry of the removed minimum node
            return minimum.getEntry()

    def min(self):
        # Get the entry with the minimum key in the priority queue
        return self.find_min().getEntry()

class SortedPQ():

    def __init__(self):
        # Constructor for SortedPQ class
        self.size = 0
        # Using a sentinel node to simplify edge cases
        self.headNode = self.tailNode = DLLNode(Entry(None, None))

    def getSize(self):
        # Get the size of the priority queue
        return self.size

    def isEmpty(self):
        # Check if the priority queue is empty
        return self.size == 0

    def insert(self, entry):
        # Insert an entry into the priority queue while maintaining order
        
        # Create a new node with the given entry
        newNode = DLLNode(entry)
        
        # Check if the priority queue is empty
        if self.isEmpty():
            # If the queue is empty, set both head and tail to the new node
            self.headNode = self.tailNode = newNode

        # Insert at the beginning, checks if the key of the entry in the newNode is less than or equal to the key of the entry in the current head node
        elif newNode.getEntry().getKey() <= self.headNode.getEntry().getKey():
            # Set the next node of the new node to the current head
            newNode.setNext(self.headNode)
            # Set the previous node of the current head to the new node
            self.headNode.setPrev(newNode)
            # Update the head to be the new node
            self.headNode = newNode

        # Insert at the end, checks if the key of the entry in the newNode is greater than or equal to the key of the entry in the current tail node
        elif newNode.getEntry().getKey() >= self.tailNode.getEntry().getKey():
            # Set the previous node of the new node to the current tail
            newNode.setPrev(self.tailNode)
            # Set the next node of the current tail to the new node
            self.tailNode.setNext(newNode)
            # Update the tail to be the new node
            self.tailNode = newNode

        # Insert in the middle
        else:
            # Start traversal from the head of the queue
            currentNode = self.headNode
            # Traverse the queue to find the insertion point, the key of the entry in the current node is less than the key of the entry in the new node
            while currentNode is not None and currentNode.getEntry().getKey() < newNode.getEntry().getKey():
                currentNode = currentNode.getNext()
            # Set the previous and next nodes of the new node
            newNode.setPrev(currentNode.getPrev())
            newNode.setNext(currentNode)
            # Update pointers of the surrounding nodes
            currentNode.getPrev().setNext(newNode)
            currentNode.setPrev(newNode)

        # Increase the size of the priority queue
        self.size += 1

    def remove_min(self):
        # Remove the entry with the minimum key from the priority queue

        if self.isEmpty():
            raise IndexError("Priority queue is empty")

        # Set the minimum node initially to the head of the queue
        minimum = self.headNode

        # Check if the queue has only one element
        if self.size == 1:
            # If there's only one element, create a new sentinel node
            # to represent an empty queue and set it as both head and tail
            self.headNode = self.tailNode = DLLNode(Entry(None, None))
        else:
            # If there is more than one element, move the head to the next node
            self.headNode = self.headNode.getNext()
            # Set the previous node of the new head to None
            self.headNode.setPrev(None)

        # Decrease the size of the priority queue
        self.size -= 1

        # Return the entry of the removed minimum node
        return minimum.getEntry()

    def min(self):
        # Get the entry with the minimum key in the priority queue
        
        # Check if the priority queue is empty
        if self.size == 0:
            # If the queue is empty, return None
            return None
        else:
            # If the queue is not empty, return the entry of the head node
            return self.headNode.getEntry()

