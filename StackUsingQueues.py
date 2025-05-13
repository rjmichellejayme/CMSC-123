import SLLQueue

class StackUsingQueues:

    def __init__(self):
        self.sll_queue = SLLQueue.SLLQueue() #initializes an instance variable named sll_queue with an instance of the class SLLQueue from the module or package SLLQueue
        self.size = 0 #keep track of the number of elements in the queue, which is currently set to 0 

    def is_empty(self):
        return self.size == 0

    def top(self): #GOAL: returns the top (most recently pushed) element of the stack without removing it
        if self.is_empty():
            raise Exception('SLLStack is empty')
        
        top_node = None #This variable will be used to store the top element of the queue
        for _ in range(self.size): # iterates self.size times
            # The top_node variable is updated with the value of the dequeued element
            top_node = self.sll_queue.dequeue() #it dequeues an element from the front of the queue (removes an element from the queue) using the dequeue method. 
            # After dequeuing an element, it immediately enqueues the same element back into the queue.
            self.sll_queue.enqueue(top_node.getValue()) # to maintain the order of elements in the queue, as dequeueing would otherwise remove the element from the queue
            # effectively rotating the elements in the queue and maintaining their original order
            # The element that was originally at the front is moved to the back, preserving the order of the other elements in the queue.
        return top_node

    def push(self, value): 
        self.sll_queue.enqueue(value) # adds the value to the stack by enqueuing it in the underlying queue
        self.size += 1

    def pop(self): #GOAL: removes and returns the top element from the stack
        if self.is_empty():
            raise Exception('SLLStack is empty')
        
        for _ in range(self.size - 1): # iterates through the elements in the stack (all except the top element) 
            # removes the front element from the queue and returns it. In this context, it dequeues an element from the bottom of the stack and returns it
            # enqueues the dequeued element back into the queue. However, it's not immediately enqueued back at the front; it's added to the end of the queue 
            # because the top element is the one that gets dequeued and re-enqueued in a different position within the queue
            self.sll_queue.enqueue(self.sll_queue.dequeue().getValue())
        self.size -= 1
        #  top element (the one left at the front of the queue after the loop) is dequeued and returned as the result of the pop operation.
        return self.sll_queue.dequeue()

# Example
# Function to reverse a list using a stack
def reverse_list(input_list):
    stack = StackUsingQueues() # creates an instance of the SLLStack class and assigns it to the stack variable
    reversed_list = [] # empty list called reversed_list is created to store the elements in reverse order

    for item in input_list: # iterates through each element in the input_list
        stack.push(item) # Push elements from the input list onto the stack

    # Pop elements from the stack to construct the reversed list
    while not stack.is_empty(): # iterate as long as the stack is not empty
        # the pop method is used to remove the top element from the stack. The .getValue() method is used to retrieve the actual value stored in the dequeued element 
        # The retrieved value is appended to the reversed_list, effectively reversing the order of elements
        reversed_list.append(stack.pop().getValue())

    return reversed_list

# Input list
original_list = [1, 2, 3, 4, 5]

# Reverse the input list using the stack
reversed_list = reverse_list(original_list)

# Print the original and reversed lists
print("Original List:", original_list)
print("Reversed List:", reversed_list)
