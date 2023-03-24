n=int(input("Enter any odd number : "))
center = row =int((n-1)/2)
col = n 
res=[]
for i in range(row):
    temp=[]
    for j in range(col):
        if center-i <= j <= center+i :
            temp.append('*')
        else:
            temp.append(' ')
    res.append(temp)
for i in res:
    print(' '.join(i))
            
