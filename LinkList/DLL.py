#singley linear linkes list 
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
class SLL:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp

    def insert(self ,new_node,pos):
        if pos ==1:                      #insert node at first position
            new_node.next= self.head
            self.head.prev=new_node
            self.head=new_node
            print("insert at 1 st pos: ")
        else:#insert node from 2nd to last position
            p=1
            temp=self.head
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
            if temp.next:#for last position

                temp.next.prev=new_node
            new_node.prev=temp
            new_node.next=temp.next
            temp.next=new_node
    def delete(self,val):
        temp=self.head
        prev=None
        if temp.data==val:#delete first value
            self.head=self.head.next
        else:
            while(temp.data!=val):
                prev=temp
                temp=temp.next
                if temp==None:
                    print("value is not present in the List")
                    return
            prev.next=temp.next
            temp=None
            print("value is deleted")



    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

List1 =SLL()
n1=Node(10)
n2=Node(20)
List1.append(n1)
List1.append(n2)
List1.append(Node(30))
List1.append(Node(40))
List1.append(Node(50))
List1.insert(Node(555),1)
List1.insert(Node(111),3)
List1.insert(Node(888),10)

List1.print()
#List1.delete(30)
#List1.print()







