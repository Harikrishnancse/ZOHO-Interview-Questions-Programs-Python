class node:
    def __init__(self,data=None):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root == None:
            self.root = node(value)
            print(value , " inserted !!! ")
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value < cur_node.data:
            if cur_node.left == None:
                cur_node.left = node(value)
                print(value , " inserted !!! ")
            else:
                self._insert(value,cur_node.left)
        elif value > cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(value)
                print(value , " inserted !!! ")
            else:
                self._insert(value,cur_node.right)

    def print_tree(self):
        print("Postorder Tree Traversal is : ")
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            self._print_tree(cur_node.right)
            print(str(cur_node.data))

    def height(self):
        if self.root != None:
            return self._height(self.root,0)
    def _height(self,cur_node , cur_height):
        if cur_node == None :
            return cur_height-1
        left_height = self._height(cur_node.left , cur_height+1 )
        right_height = self._height(cur_node.right , cur_height+1 )

        return max(left_height,right_height)

    def diameter(self):
        if self.root != None:
            l = self._height(self.root.left,1)
            r = self._height(self.root.right,1)
            return l+r
        
    
bst = BST()
cont = True
while cont == True:
    print("\n1.Insert 2.Print 3.Height 4.Diameter")
    cho = int(input("\nEnter any option :"))
    if cho == 1:
        ele = int(input("\nEnter the element to add : "))
        bst.insert(ele)
    elif cho == 2:
        bst.print_tree()
    elif cho == 3:
        print("Tree Height : ",bst.height())
    elif cho == 4:
        print("Tree Diameter : ",bst.diameter())
    else:
        cont = False
