class Entry: #(same lab6)

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def setKey(self, key):
        # Sets a new key for the entry
        self.key = key

    def getKey(self):
        # Returns the key of the entry
        return self.key

    def setValue(self, value):
        # Sets a new value for the entry
        self.value = value

    def getValue(self):
        # Returns the value of the entry
        return self.value

class Array: #(same lab2)

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.contents = [None] * capacity
        self.size = 0
        # The 'size' attribute must not exceed the 'capacity'

    def getSize(self):
        # Returns the size of the array
        return self.size

    def getCapacity(self):
        # Returns the capacity of the Array
        return self.capacity

    def isEmpty(self):
        # Returns True if the array is empty, False otherwise
        return (self.size == 0)

class ArrayDictionary(Array):

    def insert(self, key, value):
        # Inserts a new key-value pair into the array, maintaining sorted order based on keys
        new_entry = Entry(key, value)
        if self.isEmpty():
            # If the array is empty, insert the new entry at the first position
            self.contents[self.size] = new_entry
        else:
            i = self.size
			# i is > 0 and the key of the element at index i - 1 is > key of the new_entry
			# This loop essentially finds the correct position for the new entry in order
            while i > 0 and self.contents[i - 1].getKey() > new_entry.getKey():
                # Shifts elements to the right to make space for the new entry while maintaining sorted order
                self.contents[i] = self.contents[i - 1]
                i -= 1
            self.contents[i] = new_entry  # Insert the new entry at the current index i

        self.size += 1

    def remove(self, entry):
        # Removes a specific entry from the array, shifting remaining elements to the left
        if self.isEmpty():
            raise Exception("Array is empty.")
		
        removed_entry = None
        for i in range(self.size):
			#if the current element at index i in the array matches the provided entry both in terms of key and value
            if (self.contents[i].getKey() == entry.getKey()) and (self.contents[i].getValue() == entry.getValue()):
                # Finds the matching entry and removes it
                removed_entry = self.contents[i]
				# index where the matching entry was found (i) to the second-to-last index
                for j in range(i, self.size - 1):
					# shifts each element to the left by overwriting it with the value of the next element 
                    self.contents[j] = self.contents[j + 1]
				#removes the element at index i by replacing it with the next element
                self.size -= 1
                return removed_entry

    def find(self, key):
        # Finds and returns the first entry with the specified key
        if self.isEmpty():
            raise Exception("Array is empty.")

        for i in range(self.size):
			# checks if the key of the current element at index i in the array matches the provided key
            if self.contents[i].getKey() == key:
                return self.contents[i]
		# there is no entry in the array with the specified key
        return None

    def find_all(self, key):
        # Prints all entries with a specific key
        if self.isEmpty():
            raise Exception("Array is empty.")

		# initializes an empty string variable result
        result = ""
        for i in range(self.size):
			# checks if the key of the current element at index i in the array matches the provided key
            if self.contents[i].getKey() == key:
				# if a match is found appends a formatted string to the result includes the key and value of the matching entry
                result += " (" + str(self.contents[i].getKey()) + " : " + str(self.contents[i].getValue()) + ") "
        print(result)

    def entries(self):
        # Prints all entries in the array
        if self.isEmpty():
            raise Exception("Array is empty.")

        result = ""
        for i in range(self.size):
			# appends a formatted string to the result for each element includes the key and value of the current entry at index i
            result += " (" + str(self.contents[i].getKey()) + " : " + str(self.contents[i].getValue()) + ") "
        print(result)
