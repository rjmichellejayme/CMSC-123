import SLLStack

class QueueWithStacks:
    
    def __init__(self):
        self.size = 0 #keep tracks of the current number of elements
        self.primary_stack = SLLStack.SLLStack() #main stack where elements are enqueued (added) and dequeued (removed) following the FIFO order
        self.temp_stack = SLLStack.SLLStack() #auxiliary stack is used to temporarily store elements when performing enqueue and dequeue operations

    def is_empty(self):
        return self.primary_stack.isEmpty()

    def size(self):
        return self.primary_stack.size 

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        #return value of top element of p-stack by retrieving the top element or the front element of the queue and to use getvalue method to access it
        return self.primary_stack.top().getValue()

    def enqueue(self, item): # Goal: add element at the end of queue
        #temporarily move all the elements from the p-stack to a t-stack 
        while not self.primary_stack.isEmpty():
            #pop method removes the top element from the p-stack and then uses getValue to retrieve the value of that element
            #reversing the order of elements from the p-stack and putting them into the t-stack
            self.temp_stack.push(self.primary_stack.pop().getValue())
        #enqueue the new item by pushing the item onto the t-stack
        self.temp_stack.push(item)
        #reverses the elements in the t-stack with the newly enqueued item and moves them back to the p-stack
        while not self.temp_stack.isEmpty():
            #pop elements from the t-stack, retrieve their values, and push them onto the p-stack
            self.primary_stack.push(self.temp_stack.pop().getValue())
        #restores the original order of elements in the p-stack, but with the newly enqueued item at the rear of the queue
        #ensures that the newly enqueued item becomes the last element in the queue

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        #calling pop method on the p-stack, which removes and returns the top element of the stack. 
        #then, it uses the getValue method to retrieve the value of the dequeued element
        return self.primary_stack.pop().getValue()
        #removing the front item from the queue and returning it

# Example

# Create a new queue
queue = QueueWithStacks()

# Check if the queue is empty
print("Is Empty:", queue.is_empty()) # True

# Enqueue some elements
queue.enqueue("apple")
queue.enqueue("banana")
queue.enqueue("cherry")

print("Front:   ", queue.front()) #apple

# Dequeue elements 
print("Dequeue: ", queue.dequeue()) #apple
print("Dequeue: ", queue.dequeue()) #banana

# Enqueue more elements
queue.enqueue("date")
queue.enqueue("elderberry")

print("Front:   ", queue.front()) #cherry

# Dequeue the remaining elements
print("Dequeue: ", queue.dequeue()) #cherry
print("Dequeue: ", queue.dequeue()) #date

# Check if the queue is empty
print("Is Empty:", queue.is_empty()) #False

# Enqueue another element
queue.enqueue("fig")

print("Front:   ", queue.front()) #elderberry

# Dequeue the last element
print("Dequeue: ", queue.dequeue()) #elderberry

# Check if the queue is empty
print("Is Empty:", queue.is_empty()) #False

print("Dequeue: ", queue.dequeue()) 
print("Dequeue: ", queue.dequeue()) 
