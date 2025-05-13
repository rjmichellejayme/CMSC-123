class DLLNode:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value  # Initialize the value of the node
        self.nextNode = nextNode  # Initialize the reference to the next node
        self.prevNode = prevNode  # Initialize the reference to the previous node

    def setValue(self, value):
        self.value = value  # Set the value of the node

    def getValue(self):
        return self.value  # Get the value of the node

    def setNext(self, nextNode):
        self.nextNode = nextNode  # Set the reference to the next node

    def getNext(self):
        return self.nextNode  # Get the reference to the next node

    def setPrev(self, prevNode):
        self.prevNode = prevNode  # Set the reference to the previous node

    def getPrev(self):
        return self.prevNode  # Get the reference to the previous node

class DLL:
    def __init__(self):
        self.size = 0  # Initialize the size of the doubly linked list
        self.headNode = DLLNode(None)  # Initialize the head node with None
        self.tailNode = self.headNode  # Initialize the tail node as the head node
        self.tailNode.setNext(None)  # Set the next reference of the tail node to None
        self.headNode.setPrev(None)  # Set the previous reference of the head node to None

    def getSize(self):
        return self.size  # Get the current size of the doubly linked list

    def isEmpty(self):
        return self.size == 0  # Check if the doubly linked list is empty

class DLLDeque(DLL):
    def first(self):
        if self.isEmpty():
            return DLLNode(None)  # Return a node with None value if the deque is empty
        else:
            return self.headNode  # Return the head node

    def last(self):
        if self.isEmpty():
            return DLLNode(None)  # Return a node with None value if the deque is empty
        else:
            return self.tailNode  # Return the tail node

    def insertFirst(self, value):
        new_node = DLLNode(value)  # Create a new node with the given value
        self.headNode.setPrev(new_node)  # Set the previous reference of the current head node to the new node
        new_node.setNext(self.headNode)  # Set the next reference of the new node to the current head node
        new_node.setPrev(None)  # Set the previous reference of the new node to None
        self.headNode = new_node  # Update the head node to the new node
        self.size += 1  # Increase the size of the deque

    def insertLast(self, value):
        new_node = DLLNode(value)  # Create a new node with the given value
        self.tailNode.setNext(new_node)  # Set the next reference of the current tail node to the new node
        new_node.setPrev(self.tailNode)  # Set the previous reference of the new node to the current tail node
        new_node.setNext(None)  # Set the next reference of the new node to None
        self.tailNode = new_node  # Update the tail node to the new node
        self.size += 1  # Increase the size of the deque

    def removeFirst(self):
        if self.isEmpty():
            raise Exception  # Raise an exception if the deque is empty
        removed = self.headNode  # Get the node to be removed
        self.headNode = removed.getNext()  # Update the head node to the next node
        removed.setNext(None)  # Set the next reference of the removed node to None
        self.size -= 1  # Decrease the size of the deque
        return removed  # Return the removed node

    def removeLast(self):
        if self.isEmpty():
            raise Exception  # Raise an exception if the deque is empty
        removed = self.tailNode  # Get the node to be removed
        self.tailNode = removed.getPrev()  # Update the tail node to the previous node
        removed.setPrev(None)  # Set the previous reference of the removed node to None
        self.size -= 1  # Decrease the size of the deque
        return removed  # Return the removed node
