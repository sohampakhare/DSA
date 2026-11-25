#binary search tree  using Link list Implimentation
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None


class BST:
    cnt=0
    bnt=0
    def __init__(self):
        self.root=None
        

    def insert(self,new_node):
        if self.root is None:#BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:

                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
  
            print(rt.data,end=" ")
            self.inorder(rt.right)
        

    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)
          
            self.preorder(rt.right)
       
    def postorder(self,rt):
        if rt is None:
            return
        else:
            
            self.preorder(rt.left)
            self.preorder(rt.right)
            print(rt.data,end=" ")

    def findminmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\nminval : ",temp.data)
        temp=self.root
        while temp.right:
             temp=temp.right
        print("\nmax : ",temp.data)


    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False



#count only leaf node 
    def counetleafnod(self,rt):
        if rt is None:
            return
        else:
            self.counetleafnod(rt.left)
            if rt.left is None and rt.right is None:
                self.cnt+=1
          
            self.counetleafnod(rt.right)

#count only noty leaf node 
    def counetnotleafnod(self,rt):
        if rt is None:
            return
        else:
            self.counetnotleafnod(rt.left)
            if rt.left is not None or rt.right is not None:
                self.bnt+=1
          
            self.counetnotleafnod(rt.right)








    

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))             
b1.insert(Node(450))   
b1.insert(Node(5))   
b1.insert(Node(65))   
b1.insert(Node(300))
b1.insert(Node(68))   
b1.insert(Node(0))

print("\ninorder")
b1.inorder(b1.root) 

b1.counetleafnod(b1.root)
print("leafcount is : ",b1.cnt)

b1.counetnotleafnod(b1.root)
print("not leaf nodecount is : ",b1.cnt)



'''print("\ninorder")
b1.inorder(b1.root)  '''
'''print("\npreorder") 
b1.preorder(b1.root)
print("\npostorder")
b1.postorder(b1.root)
b1.findminmax()'''

'''if b1.search(61):
    print("\n Found the Node")
else:
    print("\n NOt found")'''
