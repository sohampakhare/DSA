#Write a programm to reverse a stack using queue

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
            return self.top is None
    def push(self,new_node):

        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            popped_ele=temp.data
            print("poped element",temp.data)
            self.top=self.top.next
            temp=None
            return popped_ele

    def print(self):
        temp=self.top
        print()
        print("satck element....")
        while temp:
            print (temp.data,end =" ")
            temp=temp.next
    


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
            dequed_data=temp.data
            self.front=self.front.next
            #print("delete ",temp.data)
            if self.front==None:
                self.rear=None
                print("now Queue is empty")
            temp=None
            return dequed_data
        
           
        else:
            print("Queue is empty ")

    def is_empty(self):
        return self.front is None


    def print(self):

        temp=self.front
        print("printing Linear Queue : - ",end=' ')
        while temp:
            print(temp.data,end="  ")
            temp=temp.next
        print()

def reverse_queue(q1):
    st1=stack()
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))
    st1.print()

def reverse_stack(q1):
    st1=LQueqe()
    while not q1.is_empty():
        st1.enqueue(Node(q1.pop()))
    st1.print()
        
q=LQueqe()

q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.enqueue(Node(50))
q.print()
reverse_queue(q)

st=stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(41))
st.push(Node(50))
st.push(Node(10))
st.print()
#reverse_stack(st)
