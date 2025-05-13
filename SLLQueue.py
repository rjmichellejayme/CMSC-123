# Jhoanna R. Olana - CMSC123 Lab3
class SLLNode:
	# Insert the 'SLLNode' class you created in Lab2, since they should be the same
	def __init__(self, value):
		self.setValue(value)
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
	# Insert the 'SLL' class you created in Lab2, since they should be the same
	def __init__(self):
		self.size = 0
		self.frontNode = SLLNode(None)
		self.frontNode.setNext(SLLNode(None))

	def getSize(self):
		# returns the size of the queue
		return self.size

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		return (self.size == 0)

class SLLQueue(SLL):
	# Note that class "SLLQueue" inherits the class "SLL" attributes and methods

	def front(self):
		# The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
		return self.frontNode

	def enqueue(self, value):
		# The enqueue() operation inserts an element at the end of the queue
		# [Ignore: linked list does not have a fixed size] If the capacity is full, you are not allowed to enqueue() an element to the queue
		new_node = SLLNode(value)
		
		# Case 1: Empty Queue
		if (self.isEmpty()):
			self.frontNode = new_node
		# Case 2: Non-empty queue
		# Enqueue adds a node to a tail
		# No reference to tailNode
		# --> iterate through all nodes until current node's next is None (tail's next is None)
		else:
			curr = self.frontNode
			while (curr.getNext() != None):
				curr = curr.getNext()
			curr.setNext(new_node)

		self.size += 1
			
	def dequeue(self):
		# The dequeue() operation removes the element at the front of the queue
		# This should also return the 'Element' that was removed

		# to_remove = self.frontNode
		# --> won't work
		# --> to_remove points to front
		# --> any modification to front will be reflected to to_remove
		# to_remove = SLLNode(self.frontNode.getValue())
		# other method (corresponding line in self.size == 1):
		to_remove = self.frontNode

		if (self.isEmpty()):
			raise Exception("Error: Empty queue")
		elif (self.size == 1):
			# self.frontNode.setValue(None)
			self.frontNode = SLLNode(None)
		else:
			self.frontNode = self.frontNode.getNext()
		
		# print(f"top {self.frontNode.getValue()}\tremoved {to_remove.getValue()}")
		self.size -= 1
		return to_remove

	# for debug
	def display(self):
		print(f"front: {self.front().getValue()}")
		curr = self.front()
		while (curr != None):
			print(curr.getValue())
			curr = curr.getNext()

def main():
	mySLL = SLLQueue()

	# Class instance with None parameters != NoneType Object
	# test_node = SLLNode(None)
	# print(test_node != None)

	for i in range(0, 3):
		mySLL.enqueue(i)
	mySLL.display()

	for i in range(0, 3):
		mySLL.dequeue()
	mySLL.display()

	# mySLL.enqueue(1)
	# mySLL.display()
	# mySLL.dequeue()
	# mySLL.display()

	# mySLL.dequeue()
	# mySLL.display()

if __name__=="__main__":
	main()