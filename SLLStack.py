class SLLNode:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

class SLL:
    def __init__(self):
        # Initialize an empty list with a size of 0 and no top node.
        self.size = 0
        self.topNode = None

    def isEmpty(self):
        # Check if the list is empty.
        return self.size == 0


class SLLStack(SLL):
    def top(self):
        # Get the top element of the stack.
        if self.isEmpty():
            return SLLNode(None)
        return self.topNode

    def push(self, value):
        # Push a new element onto the stack.
        newNode = SLLNode(value)
        newNode.setNext(self.topNode)
        self.topNode = newNode
        self.size += 1

    def pop(self):
        # Pop the top element from the stack.
        if self.isEmpty():
            raise Exception("pop() still working even if array is empty") #It raises an exception if the stack is empty.
        removedNode = self.topNode
        self.topNode = self.topNode.getNext()   #  It updates the topNode to the next node and decreases the size
        self.size -= 1
        return removedNode
