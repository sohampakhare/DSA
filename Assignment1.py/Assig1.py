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
        print("printing Node : ",end=" ")
        while(temp):
            print(temp.data,end="  ")
            temp=temp.next
        print()



#reverse the Link List

    def reverse(self):
        prev = None
        temp = self.head

        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev
        print("Linked List reversed successfully")




#Find Middle node and print its value

    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node value is:", slow.data)




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




#
    def con_sum(self):
        temp = self.head

        if self.head == None:
            print("Linked List is empty!")
            return

        while temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next




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
List.reverse()
List.print()
List.find_middle()
List.insert(Node(555),3)
List.insert(Node(777),5)
List.print()
List.delete(30)
List.delete(70)
List.print()
List.con_sum()




        

