class Node :
    def __init__(self,value,pr):
        self.data=value
        self.priority=pr
        self.next=None
class prorityqueue :
    def __init__(self):
        self.front=self.rear=None
    def enqueqe(self,new_node):
        if self.front==None:
            self.front=new_node#first node to be inserted
            return
        
        if self.front.priority > new_node.priority:#firsr position
            new_node.next=self.front
            self.front=new_node
            return
        else:
            temp=self.front
            while temp:
                if new_node.priority<=temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next
            prev.next=new_node
            new_node.next=temp


    def dequeu(self):
        if self.front:
            temp=self.front
            print("node deleted: ",temp.data)
            self.front=self.front.next
            temp=None
        else:
            print("queue is emptyt...")


    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

pq=prorityqueue()
        
pq.enqueqe(Node(10,2))
pq.enqueqe(Node(20,6))
pq.enqueqe(Node(30,3))
pq.enqueqe(Node(40,9))
pq.enqueqe(Node(50,1))
pq.display()
pq.dequeu()
pq.dequeu()
pq.dequeu()
pq.dequeu()
pq.dequeu()
pq.dequeu()
pq.dequeu()
pq.display()


