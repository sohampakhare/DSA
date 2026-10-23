#linear queue
class Node:
    def __init__(self,value):

        self.data=value
        self.next=None

class LQueqe:

    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node


    def dequeue(self):
        if self.rear:
            temp=self.front
            self.front=self.front.next
            print("delete ",temp.data)
            if self.front==None:
                self.rear=None
                print("now Queue is empty")
            temp=None
           
        else:
            print("Queue is empty ")


    def print(self):

        temp=self.front
        print("printing Linear Queue : - ",end=' ')
        while temp:
            print(temp.data,end="  ")
            temp=temp.next
        print()

q=LQueqe()
q.dequeue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.enqueue(Node(66))
q.enqueue(Node(77))
q.print()
q.dequeue()
q.print()


        