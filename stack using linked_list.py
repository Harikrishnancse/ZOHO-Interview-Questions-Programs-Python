class node:
    def __init__(self,value=None):
        self.prev = None
        self.data = value
        self.next = None
        
class stack_list:
    def __init__(self):
        self.head = node()
        self.top = self.head
        
    def push(self,data):
        new_node = node(data)
        cur = self.head
        pre = None
        while cur.next != None:
            pre = cur.prev
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
        self.top = new_node

    def pop(self):
        top_node = self.top
        pre = top_node.prev
        pre.next = None
        self.top = pre
        return top_node.data

    def print(self):
        cur = self.head
        print("|------",id(cur),"------|")
        print("|  Prev   : " , id(cur.prev),"|")
        print("|  Data   : " , cur.data,"|")
        print("|  Next   : " , id(cur.next),"|")
        print("|------------------------|")
        while cur.next != None:
            cur = cur.next
            print("           |")
            print("           v")
            print("|------",id(cur),"------|")
            print("|  Prev   : " , id(cur.prev),"|")
            print("|  Data   : " , cur.data,"|")
            print("|  Next   : " , id(cur.next),"|")
            print("|------------------------|")

                
stack = stack_list()
inp = input("Enter the string:")
length = len(inp)
valid = True
if length%2 == 0:  # even length string
    for i in range(0,int(length/2)):
        stack.push(inp[i])
    stack.print()
    for i in range(int(length/2),length):
        ele = stack.pop()
        if ele != inp[i]:
            valid = False
            break
else:                # odd length string
    for i in range(0,int(length/2)):
        stack.push(inp[i])
    stack.print()
    for i in range(int(length/2)+1,length):
        ele = stack.pop()
        if ele != inp[i]:
            valid = False
            break

if valid:
    print("palindrome")
else:
    print("not palindrome")
