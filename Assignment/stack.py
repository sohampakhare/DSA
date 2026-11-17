class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None

        
    def push(self,new_node):

        if self.top==None:
            self.top=new_node
            return

        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isempty():
            print("stack is underfloww")
            #return None
        else:
            temp=self.top
            #print("popped element is ",temp.data)
            self.top=self.top.next
            return temp.data
        

    def printstack(self):
        temp=self.top
        print("stack element  ",end=" ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

    def reverseString(self,string):
        temp=Stack()

        for x in string:
            temp.push(Node(x))

        print("Reverse strin" ,end=" ")
        while not temp.isempty():
            print(temp.pop(),end=" ")
        print()

    def reverse(self):
        temp=self.top
        while temp:
            s1.push(Node(temp.data))
            temp=temp.next

s=Stack()
s1=Stack()
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))
s.push(Node(60))
s.printstack()
'''s.pop()
s.pop()
s.pop()
s.printstack()'''
s.reverse()
s1.printstack()
#s.reverseString("soham")

        