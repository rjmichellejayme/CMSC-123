class Entry: #(same lab6)
    def __init__(self, key, value):
        # Constructor for Entry class
        self.key = key
        self.value = value

    # Getter and setter methods for key
    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    # Getter and setter methods for value
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class HashTableLP():
	# LINEAR PROBING
	# Note: Elements in the Array are Entries

    def __init__(self, slots=30):
        # Constructor for Linear Probing HashTable class
        self.slots = slots
        self.table = [None] * slots
        self.size = 0

    # Getter methods for size and capacity
    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.slots

    # Check if the hash table is empty
    def isEmpty(self):
        return self.size == 0

	#METHODS

    # Retrieve value associated with a key
    def get(self, key):
		# calculates the initial index where the key is expected to be stored using hash function to convert the key into a hash value 
		# modulo to ensure that the index falls within the valid range of the table
        index = HashFunction(key) % self.slots
        if self.isEmpty():
            raise Exception("Empty")
		# It continues until an empty slot is encountered
        while self.table[index] is not None:
			# checks if the key stored at the current index matches the target key
            if self.table[index].getKey() == key:
                return self.table[index].getValue()
			# otherwise, the index is incremented by 1 and wrapped around using modulo to ensure it stays within the valid range
            index = (index + 1) % self.slots
        return None

    # Insert or update an entry in the hash table
    def put(self, key, value):
        if self.size >= self.slots:
            raise Exception("Full")
        index = HashFunction(key) % self.slots
        while self.table[index] is not None:
            if self.table[index].getKey() == key:
				# if found, the associated value is updated to the new value 
                self.table[index].setValue(value)
                return
            index = (index + 1) % self.slots
        self.table[index] = Entry(key, value)
        self.size += 1

    # Remove an entry based on the key
    def remove(self, key):
        index = HashFunction(key) % self.slots
        if self.isEmpty():
            raise Exception("Empty")
        while self.table[index] is not None:
            if self.table[index].getKey() == key:
				# store the entry to be removed
                entry = self.table[index]
				# remove the entry from the hash table
                self.table[index] = None
                self.size -= 1
                return entry
			# move to the next index if not found
            index = (index + 1) % self.slots
        return None

	#ITERATOR METHODS

    # Print all keys in the hash table
    def keys(self):
        for entry in self.table:
			# Within the loop, this condition checks if the current entry is not None.
            if entry is not None:
                print(entry.getKey(), end=" ")

    # Print all values in the hash table
    def values(self):
        for entry in self.table:
            if entry is not None:
                print(entry.getValue(), end=" ")

    # Print all key-value pairs in the hash table
    def entries(self):
        for entry in self.table:
            if entry is not None:
                print(f"{entry.getKey()}:{entry.getValue()}", end=" ")

class SLLNode:
    def __init__(self, entry, nextNode=None):
        # Constructor for Single Linked List (SLL) Node
        self.entry = entry
        self.nextNode = nextNode

    # Getter and setter methods for value
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    # Getter and setter methods for the next node
    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

class SLL:
    def __init__(self, headNode=None):
        # Constructor for Single Linked List (SLL)
        self.headNode = headNode
        self.size = 0

    # Check if the linked list is empty
    def isEmpty(self):
        return self.size == 0

    # Add a new node to the end of the linked list
    def addNode(self, entry):
        node = SLLNode(entry)
		# means empty
        if self.headNode is None:
            self.headNode = node
        else:
            current = self.headNode
            while current.nextNode is not None:
				# traverse to the last node
                current = current.nextNode
			# add new node
            current.nextNode = node
        self.size += 1

    # Remove a node from the linked list based on the key
    def removeNode(self, key):
        current = self.headNode
        previous = None
        found = False

        if self.isEmpty():
            raise Exception("Empty")

        while not found and current is not None:
            if current.entry.getKey() == key:
				# set found to be true when found
                found = True
            else:
				# set prev to curr before moving to next node
                previous = current
				# move to the next node
                current = current.getNext()

        if found:
			# if no prev node
            if previous is None:
				# set next node of curr to be the new head node
                self.headNode = current.getNext()
			# if there's a prev node
            else:
				# set the next node of the prev node to the next node of the curr node
                previous.setNext(current.getNext())
            self.size -= 1
			# return curr entry of the removed node
            return current.entry
		# if not found, return none
        else:
            return None

class HashTableSC():
	# SEPARATE CHAINING
	# Note: Elements in the Array are either Entries or an SLL that contains entries with the same hash function result

    def __init__(self, slots=10):
        # Constructor for Separate Chaining HashTable class
        self.slots = slots
        self.table = [None] * slots
        self.size = 0

    # Getter methods for size and capacity
    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.slots

    # Check if the hash table is empty
    def isEmpty(self):
        return self.size == 0

	# METHODS

    # Retrieve value associated with a key
    def get(self, key):
		# calculates the initial index where the key is expected to be stored using hash function to convert the key into a hash value 
		# modulo to ensure that the index falls within the valid range of the table
        index = HashFunction(key) % self.slots
		# checks if the entry at the calculated index is None
        if self.table[index] is None:
            return None
		# If there is an entry at the calculated index
        else:
			# initializes curr to the head associated with the hash table entry at the calculated index
            current_node = self.table[index].headNode
			# continues until the end of the linked list is reached 
            while current_node is not None:
				# checks if the key stored in the current node matches the target key
                if current_node.entry.getKey() == key:
                    return current_node.entry.getValue()
				# the curr is updated to the next node 
                current_node = current_node.getNext()
            return None

    # Insert or update an entry in the hash table
    def put(self, key, value):
		# calculates index using hash function
        index = HashFunction(key) % self.slots
		# if the entry at the calculated index is None, it means that no linked list has been created yet for that index
        if self.table[index] is None:
			# a new sll is created and assigned to that index in the hash table
            self.table[index] = SLL()
		# add new entry
        self.table[index].addNode(Entry(key, value))
        self.size += 1

    # Remove an entry based on the key
    def remove(self, key):
        index = HashFunction(key) % self.slots
        if self.isEmpty():
            raise Exception("Empty")
        if self.table[index] is None:
            return None
        else:
			# calls the removeNode method on the linked list at the calculated index
            removed_entry = self.table[index].removeNode(key)
			# if the removal of the node from the linked list was successful
            if removed_entry is not None:
                self.size -= 1
            return removed_entry

	# ITERATOR METHODS

    # Print all keys in the hash table
    def keys(self):
        for slot in self.table:
			# checks if the current slot is not None, meaning that there is an entry at that position in the hash table
            if slot is not None:
				# initializes current_node to the head of the linked list associated with that slot
                current_node = slot.headNode
				# continues until the end of the linked list is reached
                while current_node is not None:
					# prints the key associated with the current node's entry using the getKey method
                    print(current_node.entry.getKey(), end=" ")
					# updated to the next node
                    current_node = current_node.getNext()

    # Print all values in the hash table
    def values(self):
        for slot in self.table:
            if slot is not None:
                current_node = slot.headNode
                while current_node is not None:
                    print(current_node.entry.getValue(), end=" ")
                    current_node = current_node.getNext()

    # Print all key-value pairs in the hash table
    def entries(self):
		# initializes a counter variable to keep track of the slot index
        count = 0
        for slot in self.table:
			# Within the loop, the slot index is incremented
            count += 1
			# checks if the current slot is not None, meaning that there is an entry at that position in the hash table
            if slot is not None:
				# initializes current_node to the head of the linked list associated with that slot
                current_node = slot.headNode
				# prints a header indicating the current slot index
                print("\n[slot]", count)
                while current_node is not None:
                    entry = current_node.entry
					# prints the key-value pair
                    print(f"{entry.getKey()}:{entry.getValue()}", end=" ")
                    current_node = current_node.getNext()

def HashFunction(key):
	# Create a hash function to be used in key mapping for the different collision handling techniques
	# This returns the index where the key is supposedly going to be stored
	# Note: The hash function will be checked based on the quality of distribution of entries
    # Hash function to determine the index for the key
	# checks if the key is of type int
    if isinstance(key, int):
        return key 
	# checks if the key is of type str
    elif isinstance(key, str):
		# calculates the hash value by summing the ASCII values of all characters in the string
        return sum(ord(char) for char in key)
	# If the key is neither an integer nor a string
    else:
        raise TypeError("Unsupported type for hashing")

def main():
	# Create a temporary hash code (I will be giving my own when you defend)
	# Call all necessary functions
	# - HashFunction()
	# - Call both HashTable functions
	# - Call all respective iterator methods
	# REQUIRED

	# LINEAR PROBING HASH TABLE 

	ht = HashTableLP(6)
	#ht.hash_function = lambda key: HashFunction(key, ht.slots)
	ht.put("one", 1)		# inserting elements
	ht.put("two", 2)
	ht.put("three", 3)
	ht.put("four", 4)
	ht.put("five", 5)
	ht.put("six", 6)


	print(ht.get("one"))	# retrieving elements
	print(ht.get("two"))
	print(ht.get("three"))

	print("Keys:")			# displaying keys, values, entries
	ht.keys()
	print("\nValues:")
	ht.values()
	print("\nEntries:")
	ht.entries()

	ht.remove("two")		# removing element 

	print("\nAfter removing 'two':")	# displaying keys, values, entries after removal
	print("Keys:")
	ht.keys()
	print("\nValues:")
	ht.values()
	print("\nEntries:")
	ht.entries()
 
	# SEPARATE CHAINING HASH TABLE 

	ht_sc = HashTableSC(3)
	#ht_sc.hash_function = lambda key: HashFunction(key, ht_sc.slots)
	ht_sc.put("apple", "red")			# insert elements
	ht_sc.put("banana", "yellow")
	ht_sc.put("orange", "orange")
	ht_sc.put("grapes", "purple")
	ht_sc.put("strawberry", "pink")
	ht_sc.put("blueberry", "blue")
	ht_sc.put("pineapple", "yellow")
	ht_sc.put("watermelon", "red and green")
	ht_sc.put("lemon", "yellow")
	ht_sc.put("kiwi", "brown and green")



	print("\nEntries:")					# displaying entries
	ht_sc.entries()

	print("\nGet values:")				# retrieving values
	print(ht_sc.get("apple"))
	print(ht_sc.get("banana"))
	print(ht_sc.get("orange"))

	print("\nKeys:")					# displaying keys, values, entries
	ht_sc.keys()
	print("\nValues:")
	ht_sc.values()
	print("\nEntries:")
	ht_sc.entries()

	ht_sc.remove("banana")				# removing an element

	print("\nAfter removing 'banana':") 	# displaying keys, values, entries after removal

	print("Keys:")
	ht_sc.keys()
	print("\nValues:")
	ht_sc.values()
	print("\nEntries:")
	ht_sc.entries()

	# HASH FUNCTION
 
	# hashCode in this case is set to 50, and its hashed value is calculated using the HashFunction
	hashCode = 50					
	hashedKey = HashFunction(hashCode)
 
	# The calculated hashedKey is then used to calculate an index by taking the modulo (%) operation with 25.
	index = hashedKey % 25
	print(f"\nHash index value for key '{hashCode}':'{index}'")

main()
