class Node:
    def __init__(self,value):# creating Node
        self.data=value
        self.next=None
class SLL:
    def __init__(self):    #appeand a New  Node
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node

#printing a Link List
#Traverse and print the node values

    def print(self):
        temp=self.head
        print("printing Node")
        while(temp):
            print(temp.data)
            temp=temp.next


#Find Middle node and print its value

    def midval(self):
        




#Insert node at a specific position

    def insert(self,New_node,pos):
        if pos==1:
            New_node.next=self.head
            self.head=New_node
            print("node insert ho gaya")
        else:
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p=p+1
            New_node.next=temp.next
            temp.next=New_node
            print("node insert ho gaya")

#Delete node
#deleting the node

    def delete(self,val):
        temp=self.head
        prev=None
        if temp.data==val:
            self.head=self.head.next
        else:
            while(temp.data!=val):
                prev=temp
                temp=temp.next
                if temp==None:
                    print("value is  not find")
                    return
            prev.next=temp.next
            temp=None
            print("value is deleterd",val)
        





List=SLL()
n1=Node(50)
n2=Node(60)

List.append(Node(10))
List.append(Node(20))
List.append(Node(30))
List.append(Node(40))
List.append(n1)
List.append(n2)
List.append(Node(70))

List.print()
List.insert(Node(555),3)
List.insert(Node(777),5)
List.print()
List.delete(30)
List.delete(70)
List.print()




        

