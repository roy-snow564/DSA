class queue:
    def __init__(self):
        self.queue = []

    def enqueued(self,element):
        self.queue.append(element)

    def dequeued(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        else:
            return self.queue.pop(0)
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def front(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        else:
            return self.queue[0]
        
    def rear(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        else:
            return self.queue[-1]

    def display(self):
        return self.queue

#__main__

myqueue=queue()
while(True):
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.isEmpty")
    print("4.front")
    print("5.rear")
    print("6.display")
    print("7.exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = int(input("Enter element to be enqueued: "))
        myqueue.enqueued(element)
        print("Element enqueued")

    elif choice == 2:
        print(myqueue.dequeued())
    
    elif choice == 3:
        print(myqueue.isEmpty())

    elif choice == 4:
        print(myqueue.front())

    elif choice == 5:
        print(myqueue.rear())

    elif choice == 6:
        print(myqueue.display())

    elif choice == 7:
        break
    else:
        print("Invalid choice")



