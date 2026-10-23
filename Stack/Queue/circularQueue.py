class Node:
    def __init__(self,value):

        self.data=value
        self.next=None

class CQueue:

    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        self.rear.next=self.front  # this line  for adding circular Queue

    def dequeue(self):
        if self.front: #at leas on enod for circular
            temp=self.front
            
          
            if self.front==self.rear:# update foe circular
                self.rear=self.front=None
                print("now Queue is empty")
                return
            else:
                self.front=self.front.next
                print("delete ",temp.data)

                self.rear.next=self.front
            temp=None
            
           
        else:
            print("Queue is empty ")

    def print(self):

        temp=self.front
        print("printing Linear Queue : - ",end=' ')
        while True:
            print(temp.data,end="  ")
            temp=temp.next
            if temp==self.front:
                break

        print()

q=CQueue()
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.print()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.print()
