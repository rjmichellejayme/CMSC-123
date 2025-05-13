# import from lab 2

class Element:
    def __init__(self, value, index):
        # Initialize an element with a given value and index
        self.value = value
        self.index = index
    # methods to set and get the value and index of the element
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getIndex(self):
        return self.index

class Array:
    def __init__(self):
        # Initialize an array with size 0 and an empty list for contents
        self.size = 0
        self.contents = []

    def isEmpty(self):
        return (self.size == 0)

    def addElement(self, value):
        # Add an element to the array
        element = Element(value, self.size)

        # Create a new list to hold the updated contents
        new_contents = [None] * (self.size + 1)

        # Copy the existing elements to the new list
        for i in range(self.size):
            new_contents[i] = self.contents[i]

        # Add the new element to the end of the new list
        new_contents[self.size] = element

        # Update the contents and size
        self.contents = new_contents
        self.size += 1

    def removeElement(self, index):
        # Remove an element from the array at a specified index
        if 0 <= index < self.size:
            # Create a new list to hold the updated contents
            new_contents = [None] * (self.size - 1)

            # Copy elements before the index
            for i in range(index):
                new_contents[i] = self.contents[i]

            # Copy elements after the index
            for i in range(index + 1, self.size):
                new_contents[i - 1] = self.contents[i]

            # Update the contents and size
            self.contents = new_contents
            self.size -= 1

class ArrayBT(Array):
    def __init__(self):
        # Initialize a binary tree array with a root index of 0
        super().__init__()
        self.rootIndex = 0

    def setRoot(self, value):
        # Set the value of the root of the binary tree
        if self.size == 0:
            self.addElement(value)
        else:
            self.contents[0].setValue(value)

    def getRoot(self):
        # Retrieve the value of the root of the binary tree
        if self.size > 0:
            return self.contents[0].getValue()
        else:
            return None

    def setLeft(self, parentIndex, value):
        # Set the left child of a node in the binary tree
        leftChildIndex = parentIndex * 2 + 1
        if parentIndex >= self.size:
            print("Index out of bounds")
            return
        if self.contents[parentIndex].getValue() is None:
            print("Parent does not exist")
            return
        while self.size <= leftChildIndex:
            self.addElement(None)

        self.contents[leftChildIndex].setValue(value)

    def setRight(self, parentIndex, value):
        # Set the right child of a node in the binary tree
        rightChildIndex = parentIndex * 2 + 2
        if parentIndex >= self.size:
            print("Index out of bounds")
            return
        if self.contents[parentIndex].getValue() is None:
            print("Parent does not exist")
            return

        while self.size <= rightChildIndex:
            self.addElement(None)

        self.contents[rightChildIndex].setValue(value)

def traverseInOrder(index, arraytree):
    # Perform an inorder traversal (left -> root -> right)
    output = []  # Initialize an empty list to store the traversal result
    if index is not None and 0 <= index < arraytree.size:
        # Check if the index is valid (not None and within the bounds of the array)
        output = output + traverseInOrder(2 * index + 1, arraytree)
        # Recursively traverse the left subtree on the left child index and append the result to the output
        output = output + [arraytree.contents[index].getValue()]
        # Append the value of the current node to the output
        output = output + traverseInOrder(2 * index + 2, arraytree)
        # Recursively traverse the right subtree and append the result to the output
    return output  # Return the final list containing the in-order traversal


def traversePreOrder(index, arraytree):
    # Perform a preorder traversal (root -> left -> right)
    output = []  # Initialize an empty list to store the traversal result
    if index is not None and 0 <= index < arraytree.size:
        # Check if the index is valid (not None and within the bounds of the array)
        output = output + [arraytree.contents[index].getValue()]
        # Append the value of the current node to the output
        output = output + traversePreOrder(2 * index + 1, arraytree)
        # Recursively traverse the left subtree and append the result to the output
        output = output + traversePreOrder(2 * index + 2, arraytree)
        # Recursively traverse the right subtree and append the result to the output
    return output  # Return the final list containing the preorder traversal

def traversePostOrder(index, arraytree):
    # Perform a postorder traversal (left -> right -> root)
    output = []  # Initialize an empty list to store the traversal result
    if index is not None and 0 <= index < arraytree.size:
        # Check if the index is valid (not None and within the bounds of the array)
        output = output + traversePostOrder(2 * index + 1, arraytree)
        # Recursively traverse the left subtree and append the result to the output
        output = output + traversePostOrder(2 * index + 2, arraytree)
        # Recursively traverse the right subtree and append the result to the output
        output = output + [arraytree.contents[index].getValue()]
        # Append the value of the current node to the output
    return output  # Return the final list containing the postorder traversal


# Example usage of the binary tree array
arraytree = ArrayBT()
arraytree.setRoot(1)
arraytree.setLeft(0, 2)
arraytree.setRight(0, 3)
arraytree.setLeft(1, 4)
arraytree.setRight(1, 5)
arraytree.setLeft(2, 6)
arraytree.setRight(2, 7)

print("Inorder Traversal:", traverseInOrder(0, arraytree))
print("Preorder Traversal:", traversePreOrder(0, arraytree))
print("Postorder Traversal:", traversePostOrder(0, arraytree))

'''
       1
   2       3
 4   5   6   7
'''

'''
let's say nga kani imo tree pa
         0
     1      2
so ang array ana kay: [0,1,2]

what if musetRight ko sa 2, like 6
         0
     1      2
               6
ani diba?
pero unsa man ang array,
[0, 1, 2, None, None, None, 6], size = 7
        or
        0
     1      2
   -   -  -    6

so mao ng naay while loop

katong second if-statement,
kay what if mu setLeft(3, 3) ko
[0, 1, 2, None, None, None, 6], index < self.size siya so oks ra pero None man siya so parent does not exist, di ka ka setLeft


'''
