import Array

class ArrBinaryTree(Array.Array):
    def __init__(self):
        Array.Array.__init__(self) #kani bai kay para nga ma call ang constructor sa Array nga class sa import
        #para naay self.size ang katong self.contents
        self.rootIndex = 0
        self.contents[self.rootIndex] = Array.Element(self.size) #basically empty nga element 
        #ang (self.size) kay index rana nga attribute

    def setRoot(self, value):
        self.contents[0].setValue(value)  #set value sa Element object brah
        self.size += 1

    def getRoot(self):
        return self.contents[0]

    def setLeft(self, parentIndex, value):
        leftChildIndex = parentIndex * 2 + 1 #kani kay formula since 0th index ko ga start
        #pero if index 1 ka ga start then index * 2 lang ni
        if parentIndex >= self.size: #kani kay what if mu setRight siya sa index 10 tapos index 4 ra diay ka kutob nabuang na
            print("Index out of bounds")
            return
        if self.contents[parentIndex].getValue() is None: # kani bai kay kuya kaayo tan-awa sa pinaka ilawm
            print("Parent does not exist")
            return
        while self.size <= leftChildIndex: #kani sad bai sa pinaka ilawm
            self.addElement(None)

        self.contents[leftChildIndex].setValue(value)

    def setRight(self, parentIndex, value):
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

#traversal bisik rana dol pareha ra sa linked binary tree
def traversePreOrder(index, arr):
    print(arr.contents[index].getValue())
    leftChildIndex = index * 2 + 1
    rightChildIndex = index * 2 + 2
    if leftChildIndex < arr.size and arr.contents[leftChildIndex].getValue(): #wala pa nilapaw sa array and dili siya None basically
        traversePreOrder(leftChildIndex, arr)
    if rightChildIndex < arr.size and arr.contents[rightChildIndex].getValue(): 
        traversePreOrder(rightChildIndex, arr)

def traverseInOrder(index, arr):
    leftChildIndex = index * 2 + 1
    rightChildIndex = index * 2 + 2
    if leftChildIndex < arr.size and arr.contents[leftChildIndex].getValue():
        traverseInOrder(leftChildIndex, arr)
    print(arr.contents[index].getValue())
    if rightChildIndex < arr.size and arr.contents[rightChildIndex].getValue():
        traverseInOrder(rightChildIndex, arr)

def traversePostOrder(index, arr):
    leftChildIndex = index * 2 + 1
    rightChildIndex = index * 2 + 2
    if leftChildIndex < arr.size and arr.contents[leftChildIndex].getValue():
        traversePostOrder(leftChildIndex, arr)
    if rightChildIndex < arr.size and arr.contents[rightChildIndex].getValue():
        traversePostOrder(rightChildIndex, arr)
    print(arr.contents[index].getValue())

binaryTree = ArrBinaryTree()
binaryTree.setRoot(1)
binaryTree.setLeft(0, 2)
binaryTree.setRight(0, 3)
binaryTree.setLeft(1, 4)
binaryTree.setRight(1, 5)
binaryTree.setLeft(2, 6)
binaryTree.setRight(2, 7)

'''
akoang kahoy:
       1
   2       3
 4   5   6   7


'''




print("size", binaryTree.size)
binaryTree.show_array()
print("preorder:")
traversePreOrder(binaryTree.rootIndex, binaryTree)
print("inorder:")
traverseInOrder(binaryTree.rootIndex, binaryTree)
print("postorder:")
traversePostOrder(binaryTree.rootIndex, binaryTree)

'''
let's say nga kani imo tree pa
         0
     1      2
so ang array ana kay: [0,1,2]
chakto?

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

that's all thank you

fee: $300.00

'''
