#Sarai Ayon
#4/23/2024
#CS240 Data Structures and Algorithms
# Data Structures HW 2: Stacks and Queues
#Stack - Implement a stack for as an array. 

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item): #adds to stack
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            print("Stack is full. Cannot push item.")

    def pop(self): #removes from stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop item.")

    def is_empty(self): #checks if stack is empty
        return len(self.stack) == 0

    def is_full(self): #checks if stack is full
        return len(self.stack) == self.capacity

    def peek(self): #returns the top item in the stack
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek item.")






# Example usage
##First, we create a Stack object with a size of 5
stack = Stack(5) 

#Check if the stack is empty or full
print("Is stack empty?", stack.is_empty())
print("Is stack full?", stack.is_full())
#This will print True for "Is stack empty?" since we haven't added any elements yet, and False for "Is stack full?" since the stack is empty.

#Here, we push the integers 1 through 5 onto the stack. Each time we push an item, it prints a message confirming the push. 
#After pushing 5 elements, the stack will be full.
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

#Check if the stack is empty or full again after pushing 5 elements, is stack empty? False, is stack full? True
print("Is stack empty?", stack.is_empty())
print("Is stack full?", stack.is_full())

#here we attempt to stack a 6th emelent, but the stack is full so it will print "Stack is full. Cannot push item."
stack.push(6)  # Trying to push into a full stack

#Here it displays the top item in the stack, which is 5
print("Top item in stack:", stack.peek())

# Popping elements from the stack 5x
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

#Check if the stack is empty or full again after popping 5 elements, is stack empty? True, is stack full? False
print("Is stack empty?", stack.is_empty())
print("Is stack full?", stack.is_full())

#here we attempt to pop 1 more element, but the stack is empty so it will print "Stack is empty. Cannot pop item."
stack.pop()  # Trying to pop from an empty stack
