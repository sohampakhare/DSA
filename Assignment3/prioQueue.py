class Node:
    
    def __init__(self,id,name,prio):
        self.id=id
        self.name=name
        self.prio=prio
        self.next=None

class prioQueue:
    def __init__(self):
        self.front=self.rear=None

    def addprocess(self,id,name,prio):#1. Add Process: Insert a process with Process ID, Process Name and Priority (enqueue)
        new_node=Node(id,name,prio)
        
        if self.front is None:
            self.front=new_node
            print("process insert")
            return

        
        if new_node.prio < self.front.prio:
            new_node.next=self.front
            self.front=new_node
            print("prosess insert")
            return
        
        t=self.front
        prev=None
        while t and t.prio <=new_node.prio:
            prev=t
            t=t.next
        new_node.next=t
        prev.next=new_node
        print("process insert")

#4. Display Processes: Display all pending processes in priority order (display_all)

    def display(self):
        if self.front is None:
            print("Queue is empty to print")
            return
        t=self.front
        while t:
            print(f"processid: {t.id} ,name: {t.name} and prio {t.prio}")
            t=t.next


#2. Execute Process: Remove the process with the highest priority (dequeue)

    def dequeue(self):
        if self.front is None:
            print("queue is empty to dequeue element")
            return
        t=self.front
        self.front=t.next
        print(f" dequeue process  {t.name}  sucessfull")
        t=None



#3. View Next Process: Display the next process to be executed (display_next)

    def display_next(self):
        if self.front is None or  self.front.next is None:
            print("there is no next process..")
            return
        
        
        t = self.front
        print(f"Next Process : Process ID: {t.id}, Name: {t.name} & Priority : {t.prio}")



#5. Count Processes: Display the total number of pending processes (count)
    def count(self):
        if self.front is None:
            print(f"Processes count : {0}")
            return

        count = 0
        t = self.front

        while t:
            count+=1
            t=t.next

        print(f"Processes count : {count}")


q=prioQueue()
q.addprocess(1,"p1",4)
q.addprocess(2,"p2",2)
q.addprocess(3,"p3",8)
q.addprocess(4,"p4",1)
q.addprocess(5,"p5",6)
q.addprocess(6,"p6",5)
q.display()
q.dequeue()
#q.display()
q.display_next()
q.count()
        


        
