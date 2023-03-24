class node:
    def __init__(self,Data=None):
        self.data=Data
        self.next=None
        
class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!= None:
            cur = cur.next
        cur.next = new_node
        print("  Data Inserted!! \n")
        
    def display(self):
        cur = self.head
        li_co=[]
        while cur.next != None:
            cur = cur.next
            li_co.append(cur.data)
        print(li_co)

    def length(self):
        list_len = 0
        cur = self.head
        while cur.next != None:
            list_len += 1
            cur = cur.next
        return list_len

    def update(self,old,new):
        cur = self.head
        found=0
        while cur.next != None:
            cur = cur.next
            if cur.data == old :
                found = 1
                cur.data = new
                print("  Element Updated !! \n")
                break
        if found == 0:
            print("  Element Not Found!! \n")

    def delete(self,data):
        cur = self.head
        found=0
        while cur.next != None:
            prev = cur
            cur = cur.next
            if cur.data == data :
                found = 1
                prev.next = cur.next
                print("  Element Removed !! \n")
                break
        if found == 0:
            print("  Element Not Found!! \n")

    def search(self,data):
        cur = self.head
        ind = 0
        found = 0
        while cur.next != None:
            cur = cur.next
            if cur.data == data:
                found = 1
                print("  Element Found at position ",ind)
                break
            ind+=1
        if found == 0 :
            print("  Element Not Found !!!")

my_link_list = linked_list()
print("-----LINKED LIST-----")
print("1.Insert  2.Display 3.Delete 4.Length 5.Update 6.Search")
while(True):
    choice=int(input("Enter the choice : "))

    if choice == 1:
        element = int(input("Enter the element to insert : "))
        my_link_list.append(element)
        
    elif choice == 2:
        my_link_list.display()

    elif choice == 3:
        element = int(input("Enter the element to delete : "))
        my_link_list.delete(element)

    elif choice == 4:
        print(" Total No of Elements in Linked List : " , my_link_list.length(),"\n")

    elif choice == 5:
        old = int(input("Enter the existing element : "))
        new = int(input("Enter the element to be updated : "))
        my_link_list.update(old,new)
        
    elif choice == 6:
        element = int(input("Enter the element to search : "))
        my_link_list.search(element)
    else:
        print("Invalid choice")

    
        
