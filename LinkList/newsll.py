#singley linear linkes list 
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
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
    def insert(self ,new_node,pos):
        if pos ==1:                      #insert node at first position
            new_node.next= self.head
            self.head=new_node
        else:#insert node from 2nd to last position
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
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
            print(temp.data)
            temp=temp.next

List1 =SLL()
n1=Node(10)
n2=Node(20)
List1.append(n1)
List1.append(n2)
List1.append(Node(30))
List1.append(Node(40))
List1.insert(Node(555),3)

List1.print()
List1.delete(30)
List1.print()







