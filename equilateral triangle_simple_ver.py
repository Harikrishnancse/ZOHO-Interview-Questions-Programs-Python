n = int(input("Enter the number : "))
res=[]
for i in range(n):
    temp=[]
    for j in range(0,n-i-1):
        #temp.append('-')
        temp.append(' ')
    #temp.append('/')
    for j in range(0,2*i+1):
        temp.append('*')
    #temp.append('\\')
    res.append(temp)
#res.append(['-' for i in range(n+n+1)])

print("Equilateral triangle is : \n")
for i in res:
    print(''.join(i))

print("Hourglass pattern is : \n")
hg = res[:0:-1] + res
for i in hg:
    print(''.join(i))
