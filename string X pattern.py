string=str(input("Enter the input:"))
out=[]
for i in range(len(string)):
    temp=[]
    for j in range(len(string)):
        if i==j or i+j==len(string)-1 :
            temp.append(string[j])
        else:
            temp.append(' ')
    out.append(temp)
for i in out:
    print(' '.join(i))
