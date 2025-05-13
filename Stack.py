# Jhoanna R. Olana - Lab 2

# Implementation of stack in an array
# Does not use python list functions
# If allowed, should do:
# self.contents = []
# in push: use append
# in pop: use pop

class Element:
	def __init__(self, value, index):
		self.setValue(value)
		self.index = index

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

	def getIndex(self):
		return self.index

class Array:
	def __init__(self, capacity = 10):
		# intialized to be able to access array using indices
		# each cell in a python list references to a value (unlike in C array which stores a value)
		self.contents = [None] * capacity
		# self.contents = []
		# Stack: array_top == array_last
		# array size == self.size == placeholder for the next top
		# --> in push: index(new_top) == self.size
		# --> in pop: index(top) == self.size - 1
		self.size = 0 				# The 'size' attribute must not exceed the 'capacity' 	
		self.capacity = capacity
		self.DEFAULT_EXPANSION = 5

	def getCapacity(self):
		return self.capacity

	def isEmpty(self):
		# The isEmpty() operation returns true if the stack is empty and false if the stack is not empty
		return (self.size == 0)

	def expand(self):
		# The expand() operation increases the capacity when necessary
		self.capacity += self.DEFAULT_EXPANSION

class ArrayStack(Array):
	# to visualize:
		# contents = [None, None, ... None] (# of Nones = 10)
		# assume we pushed 3 times
		# --> contents = [pushed1, pushed2, pushed3, None, None, ... None] (# of Nones = 7)
		# --> top = pushed3	size = 3 top_index = 3 - 1 = 2
		# if contents[top_index] == contents[2] is popped
		# --> contents = [pushed1, pushed2, None, None, None, ... None] (# of Nones = 8)
		# --> top = pushed2 size = 2 top_index = 2 - 1 = 1
	
	# Note that class "ArrayStack" inherits the class "Array" attributes and methods

	def top(self):
		# The top() operation returns a reference value to the top element of the stack, but doesn’t remove 

		if (self.isEmpty()):
			return Element(None, None)
		else:	
			# can't use -1 because the last element in the contents is None
			# as it was intialized like that (line 26)
			# to see, run:
			# print(self.contents[-1])
			return self.contents[self.size - 1]

	def push(self, value):
		# The push() operation inserts an item at the top of the stack
		# If the capacity is full, you are not allowed to push() an item to the stack

		if (self.size == self.getCapacity()):
			raise Exception("Error: Full stack")
		# Note: pushing means putting an element in the (last + 1)th element
		# --> different algo when pushing to an empty stack
		elif (self.size == 0):
			self.contents[0] = Element(value, 0)
		else:
			self.contents[self.size] = Element(value, self.size)

		# if built-in function allowed: (same reason with pop)
		# self.contents.append(value)
		self.size += 1

	def pop(self):
		# The pop() operation removes the item at the top of the stack
		# This should also return the 'Element' that was removed

		to_remove = self.top()
		i = to_remove.getIndex()

		if (self.isEmpty()):
			raise Exception("Error: Empty Stack")
		else:
			self.contents[i] = None

		# if built-in function allowed: pop function can be shortened to the following lines of code
		# (catching for empty stack should still be remained)
		# self.contents.pop()
		self.size -= 1
		return to_remove

	# for debug
	def display(self):
		if (self.isEmpty()):
			print("! Can't display nothing")
			
		print(f"size: {self.size}\tcapacity: {self.capacity}\ntop: {self.top().getValue()}")
		for i in range(0, self.size):
			print(f"self.contents[{i}]: {self.contents[i].getValue()}")

def main():
	myArr = ArrayStack()

	print(myArr.size, myArr.getCapacity())
	# for i in range(10):
	# 	# print(i)
	# 	myArr.push(i)
	# myArr.display()

	# myArr.push(11)
	# myArr.pop()
	# myArr.push(11)
	
	# for i in range(12):
	# 	print(f"Remove {i}")
	# 	myArr.pop()
	# myArr.display()

	myArr.push(1)
	myArr.display()
	myArr.pop()
	myArr.display

if __name__ == "__main__":
	main()
