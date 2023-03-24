class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None
        self.arr = []

    def tree_sum(self,root):
        if root.left==None and root.right==None:
            return root.data
        elif root.left!=None and root.right==None:
            return root.data + self.tree_sum(root.left)
        elif root.left==None and root.right!=None:
            return root.data + self.tree_sum(root.right)
        else:
            return root.data + self.tree_sum(root.left) + self.tree_sum(root.right)

    def find_sum(self,root):
      pass
            
            

bt = BT()
bt.root = Node(8)
bt.root.left = Node(4)
bt.root.right = Node(1)
bt.root.left.left = Node(6)
bt.root.left.right = Node(7)
bt.root.right.right = Node(5)
bt.tree_sum(bt.root)
print(bt.arr)

