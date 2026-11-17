class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None


    def isEmpty(self):
        return self.rear == None


    def enque(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = self.rear = newNode
            return

        self.rear.next = newNode
        self.rear = newNode


    def deque(self):
        if self.isEmpty():
            print("Queue underflow!")
            return 

        t = self.front
        self.front = self.front.next
        t.next = None
        t= None


    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return

        t= self.front
        print("Queue Elements: ")
        while t:
            print(t.data,end=" ")
            t=t.next
        print()

    def reverse(self):
        top =-1
        stack = []
        t = self.front

        while t:
            top+=1
            stack.append(t.data)
            t=t.next

        t= self.front
        while t:
            t.data = stack[top]
            top-=1
            t=t.next

    def mergeQueues(self,queue2):
        mergedQueue = Queue()
        t = self.front
        while t:
            mergedQueue.enque(t.data)
            t=t.next

        t = queue2.front
        while t:
            mergedQueue.enque(t.data)
            t=t.next

        return mergedQueue

    def areQueuesIdentical(self,queue2):

        t = self.front
        q = queue2.front

        while t and q:
            if  t.data != q.data:
                print("Queues are not identical!")
                return

            t=t.next
            q=q.next

        print("Queues are Identical!")
        



queue1 = Queue()
queue1.enque(10)
queue1.enque(20)
queue1.enque(30)
queue1.enque(40)
queue1.enque(50)
queue1.enque(60)
queue1.display()

#queue1.reverse()
#queue1.display()
'''queue1.deque()
queue1.deque()
queue1.deque()
queue1.display()'''
'''# queue.enque(50)
# queue.display()
# queue.deque
# queue.display()
#queue.reverse()
# queue.display()'''
queue2 = Queue()
queue2.enque(11)
queue2.enque(22)
queue2.enque(33)
queue2.enque(44)
queue2.display()

#mergedQueue = queue1.mergeQueues(queue2)
#mergedQueue.display()

queue1.areQueuesIdentical(queue2)