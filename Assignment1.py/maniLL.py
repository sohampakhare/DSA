#Class for creating Nodes
class Node:

    def _init_(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head=None

    #function for inserting a node at the end of LL
    def append(self,data):
        newNode = Node(data)
        #Checking if LL is empty!
        if self.head==None:
            self.head = newNode
            return

        #Traversing till end of ll and adding the new node!
        t = self.head
        while t.next:
            t=t.next
        t.next=newNode

    
    def traverse(self):
        #Checking if LL is empty!
        if self.head==None:
            print("LinkeedList is empty!")
            return

        #traversing till Node is node and printing its Node values!
        t = self.head
        while t:
            print(t.data,end=" -> ")
            t=t.next
        print("None")

    #Function for inserting a node at given position
    def insert(self,posi,data):
        #Checking if LL is empty and posi is greater than 1 (Index out of bounds)
        if self.head == None and posi != 1:
            print("Linked List is empty!")
            print("Cannot insert at given position")
            return

        newNode=Node(data)
        #If position is 1 assigning newNodes.next as head and head as newNode
        if  posi == 1:
            newNode.next= self.head
            self.head = newNode
            return

        #If position is greater than 1. Traversing till posi -1 to insert newNode at given position
        count = 1
        t = self.head
        while(count != (posi -1)):
            #Checking if given position is out of bounds! (position is higher than Nodes in LL)
            if t == None:
                print("Index out of bounds!")
                return
            t=t.next
            count+=1
        newNode.next = t.next
        t.next = newNode

    #function to find middle Node
    def findMidNode(self):
        #Checking if LL is empty!
        if self.head == None:
            print("Linked List is empty!")
            return

        #Loop to check total no of nodes in LL
        total = 0
        t = self.head
        while t != None:
            total+=1
            t=t.next

        #Logic to find middle node by checking if no is even or odd.
        mid = total //2
        if total % 2 != 0:
            mid+=1
        count =1
        t = self.head
        #Loop to traverse till mid element and print its value!
        while count != mid:
            t=t.next
            count+=1
        print(f"Middle Node Value: {t.data}")

        #Function to delete a node by given position
    def deleteByIndex(self,posi):
        #checking if LL is empty!
        if self.head == None:
            print("Linked List is empty cannot delete!")
            return

        #If posi = 1, shifting head to head.next
        if posi ==1:
            self.head=self.head.next
            return

        #if posi >1 traversing to posi -1 node
        count = 1
        t = self.head
        while count != (posi - 1):
            #Logic to check if position is out of bounds!
            if t == None:
                print("Index out of bounds!")
                return
            t=t.next
            count+=1
        #Logic to check if position is out of bounds!
        if t.next == None:
            print("Index out of bounds!")
            return
        t.next= t.next.next

    #Function to reverse a linked list
    def reverse(self):
        #checking if LL is empty!
        if self.head == None:
            print("Linked List is empty!")
            return
        #add all node values in a list
        result = []
        t = self.head
        while t:
            result.append(t.data)
            t=t.next

        #traversing linked list and assigning values in reverse of the result list
        t = self.head
        k = len(result)-1
        while t:
            t.data = result[k]
            k-=1
            t=t.next

    #function to print consecutive sum in LL
    def printConsecutiveValues(self):
        #checking if LL is empty
        if self.head == None:
            print("Linked List is empty!")
            return

        t = self.head
        i=1
        #Logic to pring consecutive sums
        while t.next:
            sum = t.data + t.next.data
            print(f"Sum of {i} + {i+1} nodes: {sum}",)
            i+=1
            t=t.next



if _name_ == "_main_":
    # Write your solution here
    ll= LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.traverse()
    ll.insert(2,66)
    ll.traverse()
    ll.insert(1,100)
    ll.traverse()
    ll.findMidNode()
    ll.insert(1,999)
    ll.traverse()
    ll.insert(7,1234)
    ll.traverse()
    ll.findMidNode()
    ll.deleteByIndex(7)
    ll.traverse()
    ll.reverse()
    ll.traverse()
    ll.printConsecutiveValues()