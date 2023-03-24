special = ['@',' ','#','$','_']
inp = input("Enter the string : ")
res = ""
stack = []
for i in range(len(inp)):
    if inp[i] not in special:
        stack.append(inp[i])
for i in range(len(inp)):
    if inp[i] not in special:
        t =  stack.pop()
        res = res + t
    else:
        res = res + inp[i]
print(res)
