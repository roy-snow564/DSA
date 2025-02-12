class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def stacksize(self):
        return len(self.stack)
    
    def display(self):
        return self.stack
    
#__main__

Stack=stack()
while(True):
    print("\nStack Operations:")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Stack Size")
    print("5.display")
    print("6.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        element=int(input("Enter the element to be pushed:"))
        Stack.push(element)
        print("Element pushed successfully")
    elif choice==2:
        print("Popped element is:",Stack.pop())
    elif choice==3:
        print("Top element is:",Stack.peek())
    elif choice==4:
        print("Stack size is:",Stack.stacksize())
    elif choice==5:
        print("Stack elements are:",Stack.display())
    elif choice==6:
        break
    else:
        print("Invalid choice")
        


