class BTNode:
    def __init__(self, value):
        # Initialize a binary tree node with a given value
        self.value = value
        self.parentNode = None
        self.leftChildNode = None
        self.rightChildNode = None

    def setValue(self, value):
        # Set the value of the node
        self.value = value

    def getValue(self):
        # Get the value of the node
        return self.value

    def setParent(self, parent):
        # Set the parent node
        self.parentNode = parent

    def getParent(self):
        # Get the parent node
        return self.parentNode

    def setLeft(self, leftChildNode):
        # Set the left child node
        self.leftChildNode = leftChildNode

    def getLeft(self):
        # Get the left child node
        return self.leftChildNode

    def setRight(self, rightChildNode):
        # Set the right child node
        self.rightChildNode = rightChildNode

    def getRight(self):
        # Get the right child node
        return self.rightChildNode


class LinkedBT:
    def __init__(self):
        # Initialize a linked binary tree with a root node and size 0
        self.rootNode = None
        self.size = 0

    def getSize(self):
        # Get the size of the tree
        return self.size

    def isEmpty(self):
        # Check if the tree is empty
        return self.size == 0

    def setRoot(self, value):
        # Creates a new BTNode with the specified value and sets it as the root of the tree
        root = BTNode(value)
        self.rootNode = root

    def getRoot(self):
        # Get the root of the tree
        return self.rootNode

    def setLeft(self, parentNode, value):
        #Creates a new left child node with the specified value and sets it as the left child of the given parentNode
        child = BTNode(value)
        child.setParent(parentNode)
        parentNode.setLeft(child)

    def setRight(self, parentNode, value):
        # Creates a new right child node with the specified value and sets it as the right child of the given parentNode
        child = BTNode(value)
        child.setParent(parentNode)
        parentNode.setRight(child)


# Tree Traversals
def inorderTraversal(node):
    # Perform an inorder traversal (left -> root -> right)
    output = []  # Initialize an empty list to store the traversal result

    # Base Case: Check if the current node is not None
    if node is not None:
        left = node.getLeft()  # Retrieve the left child node
        right = node.getRight()  # Retrieve the right child node

        # Recursively traverse the left subtree and extend the output list
        output.extend(inorderTraversal(left))

        value = node.getValue()  # Retrieve the value of the current node
        output.append(value)  # Append the value to the output list

        # Recursively traverse the right subtree and extend the output list
        output.extend(inorderTraversal(right))

    return output  # Return the final list containing the values of the nodes in the correct order



def preorderTraversal(node):
    # Perform a preorder traversal (root -> left -> right)
    output = []  # Initialize an empty list to store the traversal result

    # Base Case: Check if the current node is not None
    if node is not None:
        left = node.getLeft()  # Retrieve the left child node
        right = node.getRight()  # Retrieve the right child node

        value = node.getValue()  # Retrieve the value of the current node
        output.append(value)  # Append the value to the output list

        # Recursively traverse the left subtree and extend the output list
        output.extend(preorderTraversal(left))

        # Recursively traverse the right subtree and extend the output list
        output.extend(preorderTraversal(right))

    return output  # Return the final list containing the values of the nodes in the correct order



def postorderTraversal(node):
    # Perform a postorder traversal (left -> right -> root)
    output = []  # Initialize an empty list to store the traversal result

    # Base Case: Check if the current node is not None
    if node is not None:
        left = node.getLeft()  # Retrieve the left child node
        right = node.getRight()  # Retrieve the right child node

        # Recursively traverse the left subtree and extend the output list
        output.extend(postorderTraversal(left))

        # Recursively traverse the right subtree and extend the output list
        output.extend(postorderTraversal(right))

        value = node.getValue()  # Retrieve the value of the current node
        output.append(value)  # Append the value to the output list

    return output  # Return the final list containing the values of the nodes in the correct order


#      1
#     /  \
#   2      3
#  /  \
# 4    5

linkedtree = LinkedBT()
linkedtree.setRoot(1)
root = linkedtree.getRoot()

linkedtree.setLeft(root, 2)
linkedtree.setLeft(root.getLeft(), 4)
linkedtree.setRight(root.getLeft(), 5)

linkedtree.setRight(root, 3)

# Perform tree traversals
inorder = inorderTraversal(root)
preorder = preorderTraversal(root)
postorder = postorderTraversal(root)

print("Inorder Traversal:", inorder)
print("Preorder Traversal:", preorder)
print("Postorder Traversal:", postorder)
