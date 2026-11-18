class Node:

    def _init_(self,id,name,prio):
        self.id = id
        self.name = name
        self.prio = prio
        self.next = None


class PriorityQueue:

    def _init_(self):
        self.front = self.rear = None


    def addProcess(self,id,name,prio):
        newNode = Node(id,name,prio)
        if self.front is None:
            self.front = newNode
            print("Inserted Process")
            return

        if newNode.prio < self.front.prio:
            newNode.next = self.front
            self.front = newNode
            print("Inserted Process")
            return

        t = self.front
        prev = None

        while t and t.prio <= newNode.prio:
            prev = t
            t=t.next

        newNode.next = t
        prev.next = newNode
        print("Inserted Process")



    def display_all(self):
        if self.front is None:
            print("Queue underflow!")
            return

        t = self.front
        while t:
            print(f"Process ID: {t.id}, Name: {t.name} & Priority : {t.prio}")
            t=t.next

        print("--------------------")

    def deque(self):
        if self.front is None:
            print("Queue underflow!")
            return

        t = self.front

        self.front = t.next

        print(f"Executed Process : {t.name}!")
        t = None

    def display_next(self):
        if self.front is None or self.front.next is None:
            print("Theres no next process!")
            return

        t = self.front
        print(f"Next Process : Process ID: {t.id}, Name: {t.name} & Priority : {t.prio}")

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


PQ = PriorityQueue()
PQ.addProcess(1,"P1",4)
PQ.addProcess(2,"P2",2)
PQ.addProcess(3,"P3",1)
PQ.addProcess(4,"P4",3)
PQ.addProcess(5,"P4",1)
PQ.display_all()
PQ.deque()
PQ.display_all()
PQ.display_next()
PQ.count()