n=int(input("Enter any number : "))
row = n
col = (2*n)-1 #n+(n-1)
center = (col-1)/2
res=[]
for i in range(row):
    temp=[]
    for j in range(col):
        if center-i <= j <= center+i:
            if (i+j)%2 == 0 :
                temp.append('*')
            else:
                temp.append(' ')
        else:
            temp.append(' ')
    res.append(temp)
for i in res:
    print(' '.join(i))
            
