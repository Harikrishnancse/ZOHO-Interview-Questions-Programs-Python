inp = input("Enter the string : ")
string = ""
for i in range(0,len(inp)):
    if i+1 < len(inp) and inp[i]==')' and inp[i+1] == '(' :
            string = string + inp[i] + "*"
    else:
        string += inp[i]
alpha = ['a','b','c','d','e','temp_res']
oper = ['+','-','*','/']
stack = []
status = True
for char in string:
    if char in ['(']:
        stack.append(char)
    elif char in alpha:
        stack.append(char)
    elif char in oper:
        stack.append(char)
    elif char == ')':
        if '(' in stack:
            b = stack.pop()
            op = stack.pop()
            a = stack.pop()
            if a not in alpha or b not in alpha or op not in oper:
                status = False
                break
            stack.pop()
            stack.append('temp_res')
        else:
            status = False
            break
        
if len(stack)== 1 and stack[0] == 'temp_res' :
    stack.pop()
elif len(stack)== 3 and stack[0] == 'temp_res' and stack[2] == 'temp_res' and stack[1] in oper :
    stack = []

if stack ==[] and status == True :
    print('Valid!!!')
else:
    print('Invalid!!!')
        
        
        

