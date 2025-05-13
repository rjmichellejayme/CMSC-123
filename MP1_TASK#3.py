class Element:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def getValue(self):
        return self.value

    def getIndex(self):
        return self.index

class Array:
    def __init__(self, capacity=10):
        self.contents = [None] * capacity
        self.size = 0
        self.capacity = capacity
        self.DEFAULT_EXPANSION = 5

    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def expand(self):
        self.capacity += self.DEFAULT_EXPANSION
        new_contents = [None] * self.capacity
        for i in range(self.getSize()):
            new_contents[i] = self.contents[i]
        self.contents = new_contents

class ArrayStack(Array):
    def top(self):
        if not self.isEmpty():
            return self.contents[self.getSize() - 1]
        else:
            return None

    def push(self, value):
        if self.getSize() < self.getCapacity():
            element = Element(value, self.getSize())
            self.contents[self.getSize()] = element
            self.size += 1
        else:
            self.expand()
            element = Element(value, self.getSize())
            self.contents[self.getSize()] = element
            self.size += 1

    def pop(self):
        if not self.isEmpty():
            element = self.contents[self.getSize() - 1]
            self.size -= 1
        else:
            raise Exception("Stack is Empty")
        return element

class Palindrome:
    def __init__(self):
        self.stack = ArrayStack()

    def isPalindrome(self, word):
        word = word.lower()
        new_word = ""
        for i in word:
            if i != " ":
                new_word += i

        for i in new_word:
            self.stack.push(i)

        reverseWord = ""
        while not self.stack.isEmpty():
            reverseWord += self.stack.pop().getValue()

        return new_word == reverseWord

    def main(self):
        checkWord = input("Enter a word: ")
        if not checkWord:
            print("Please provide a word")
        else:
            if self.isPalindrome(checkWord):
                print("It is a Palindrome")
            else:
                print("Not a Palindrome")
            while True:
                choice = input("Would you like to run the program again? (Y/N)\n")
                if choice.lower() == 'y':
                    self.main()
                elif choice.lower() == 'n':
                    exit()
                else:
                    print("Invalid input. Please try again")

if __name__ == "__main__":
    palindrome = Palindrome()
    palindrome.main()
