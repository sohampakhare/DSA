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
