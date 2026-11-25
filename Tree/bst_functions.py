class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, new_node):
        if self.root is None:   # if bst is empty
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def findminmax(self, rt):
        if self.root is None:
            print("Empty tree")
        else:
            # Minimum
            temp = self.root
            while temp.left is not None:
                temp = temp.left
            print("Minimum value is",temp.data)
            # Maximum
            temp = self.root
            while temp.right is not None:
                temp = temp.right
                print("Maximum value is",temp.data)

    def del_node(self, rt, val):
        if rt is None:
            return
        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left

            # when node has both left and right child (succ = successor)
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)
            return rt

    def get_successor(self, temp):
        temp = temp.right
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp

b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))

print("Inorder:")
b1.inorder(b1.root)
print("\nPreorder:")
b1.preorder(b1.root)
print("\nPostorder:")
b1.postorder(b1.root)
print()
b1.findminmax(b1.root)

b1.del_node(b1.root, 10)
b1.inorder(b1.root)