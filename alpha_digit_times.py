string = input("Enter string : ")
stack=[]
digit=['1','2','3','4','5','6','7','8','9','0']
res=""
i=0
while i<len(string):
    if string[i] in digit:
        if string[i+1] in digit:
            times = (int(string[i])*10) + int(string[i+1])
            i+=1
        else:
            times = int(string[i])
        char = stack.pop()
        new = char * times
        res += new
    else:
        stack.append(string[i])
    i+=1
print(res)
            
        
