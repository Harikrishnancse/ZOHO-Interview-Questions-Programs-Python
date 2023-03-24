inp = input("enter the original string : ")
search = input("enter the search string : ")
found = False
for i in range(0,len(inp)):
    temp = inp[ i : i+len(search) ]
    if temp == search:
        found = True
        print(i)
        break
if not found:
    print('-1')

    

