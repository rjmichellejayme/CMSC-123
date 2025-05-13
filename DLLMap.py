class Entry:
	# Use the 'Entry' class used in Lab6, since they should be relatively the same
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def setKey(self,key):
		self.key = key

	def getKey(self):
		return self.key

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

class DLLNode:
	# Use the 'DLLNode' class used in Lab6, since they should be relatively the same
	def __init__(self, entry, nextNode=None, prevNode=None):
		self.entry = entry
		self.nextNode = nextNode
		self.prevNode = prevNode

	def setEntry(self,entry):
		self.entry = entry

	def getEntry(self):
		return self.entry

	def setNext(self,nextNode):
		self.nextNode = nextNode

	def getNext(self):
		return self.nextNode

	def setPrev(self,prevNode):
		self.prevNode = prevNode

	def getPrev(self):
		return self.prevNode

class DLLMap():
	def __init__(self):
		self.size = 0
		self.headNode = self.tailNode = DLLNode(None)

	def getSize(self):
		# returns the size of the queue
		return self.size

	def isEmpty(self):
		# The isEmpty() returns true if the queue is empty and false if the queue is not empty
		return (self.size == 0)

	def find_node(self, key):
		# Initializes a variable current with the head node 
		current = self.headNode
		# loop continues as long as current node has the next node
		while current.getNext() != None: 
			# checks if the key of the entry stored in the current node is equal to the target key
			if current.getEntry().getKey() == key: 
				return current
			# if not equal, the loop continues to the next node in the list
			current = current.getNext() 
	
		return current

	def get(self, key):
		# finds and returns the value of the entry with the specified key
		if self.isEmpty():
			raise Exception("Empty Map")

		# Calls the find_node method to locate the node within the map that corresponds to the specified key. 
		entry = self.find_node(key) 
		return entry.getEntry().getValue()

	def put(self, key, value):
		# inserts an entry with the specified key and value in the map; overwrites existing entry if key already exists
		entry = DLLNode(Entry(key, value))

		if self.isEmpty():
			# set head and tail to the newly created entry
			self.headNode = self.tailNode = entry 
			self.size += 1
		# Checks if the key of the new entry is less than or equal to the key of the head node
		elif self.headNode.getEntry().getKey() >= entry.getEntry().getKey():
			# if equal, it updates the head node's entry with the new entry's data
			if self.headNode.getEntry().getKey() == entry.getEntry().getKey():
				self.headNode.setEntry(entry.getEntry())
			# if the head node's key is greater, it inserts the new entry before the head node
			else: 
				entry.setNext(self.headNode)
				self.headNode.setPrev(entry)
				self.headNode = entry
				self.size += 1
		# Checks if the key of the new entry is greater than or equal to the key of the tail node.
		elif self.tailNode.getEntry().getKey() <= entry.getEntry().getKey():
			# if equal, it updates the tail node's entry with the new entry's data
			if self.tailNode.getEntry().getKey() == entry.getEntry().getKey():
				self.tailNode.setEntry(entry.getEntry())
			# if the tail node's key is less, it inserts the new entry after the tail node
			else:
				self.tailNode.setNext(entry)
				entry.setPrev(self.tailNode)
				self.tailNode = entry
				self.size += 1
		# If the new entry needs to be inserted in the middle of the list, a loop is used to find the appropriate position.
		else: 
			current = self.headNode
			# If the key of the current entry is equal to the key of the new entry
			while current.getNext() != None and current.getNext().getEntry().getKey() <= entry.getEntry().getKey():
				# if equal, update the current entry's data with the new entry's data and return
				if current.getEntry().getKey() == entry.getEntry().getKey():
					current.setEntry(entry.getEntry())
					return
				#if the key of the next entry is equal to the key of the new entry
				elif current.getNext().getEntry().getKey() == entry.getEntry().getKey():
					# update the next entry's data with the new entry's data and return
					current.getNext().setEntry(entry.getEntry())
					return
				# Move to the next node in the linked list
				current = current.getNext()
			entry.setNext(current.getNext())
			entry.setPrev(current)
			current.setNext(entry)
			current.getNext().setPrev(entry)
			self.size += 1


	def remove(self, key):
		# removes the entry with the specified key, and returns the entry that was removed
		if (self.isEmpty()):
			raise Exception("Empty Map")
		# otherwise, calls the find_node method to locate the node that corresponds to the specified key
		remove = self.find_node(key)

		# Checks if there is only one node, meaning that the map contains only one entry.
		if self.headNode == self.tailNode:
		# sets both the head and tail nodes to a new DLLNode(None) creating an empty node
			self.headNode = self.tailNode = DLLNode(None) 

		# Checks if the node to be removed is the head node.
		elif remove == self.headNode:
			# updates the head node to be the next node in the list, skipping the current head node
			self.headNode = self.headNode.getNext()

		# Checks if the node to be removed is the tail node.
		elif remove == self.tailNode:
			# updates the tail node to be the previous node in the list, skipping the current tail node
			self.tailNode = self.tailNode.getPrev()

		# If the node to be removed is neither the head nor the tail, it means the removal is from the middle of the list
		else:
			# adjusts the pointers of the previous and next nodes of the node to be removed
			remove.getPrev().setNext(remove.getNext())
			remove.getNext().setPrev(remove.getPrev())


		self.size -= 1
		return remove.getEntry()

	# Iterator Methods
	def keys(self):
		# initializes an empty string that will be used to concatenate the keys during the iteration.
		string = ""
		current = self.headNode
		# Enters a while loop that continues as long as there are nodes
		while current != None:
			# Appends the formatted string that converts the key of the current entry into a string and concatenates it with parentheses
			string += " (" + (str(current.getEntry().getKey())) + ") "
			current = current.getNext()
		print(string)

	def values(self):
		# iterates through the existing entries in the map and prints all the values in order
		string = ""
		current = self.headNode
		while current != None:
			string += " (" + (str(current.getEntry().getValue())) + ") "
			current = current.getNext() 
		print(string) 

	def entries(self):
		# iterates through the existing entries in the map and prints all the entries (in the format "key:value") in order
		string = ""
		current = self.headNode
		while current != None:
			string += " (" + (str(current.getEntry().getKey())) + " : " + (str(current.getEntry().getValue())) + ") "
			current = current.getNext()
		print(string)