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


# reverse the Link List
    def rev(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev


#deleting the Linl list

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
#find middle node and delete the Noide

    def find_mid(self):
        temp=temp1=self.head
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp.next.next
        print("middle Node ",temp.data)
        prev.next=temp.next
        temp=None

#delete first and last node

    def fl_del(self):

        self.head=self.head.next
        print("first nodde delete")
        temp=self.head
        while temp.next:
            prev=temp
            temp=temp.next

        prev.next=None
        temp=None
        print("Last nodde delete")

            
            



    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()
List1 =SLL()
n1=Node(10)
n2=Node(20)
List1.append(n1)
List1.append(n2)
List1.append(Node(30))
List1.append(Node(40))
List1.insert(Node(555),3)
List1.append(Node(60))
List1.append(Node(70))

List1.print()
List1.delete(30)
List1.print()
List1.rev()
List1.print()
List1.find_mid()
List1.print()
List1.fl_del()
List1.print()








