num = int(input("Enter the number : "))
lis = [[1],[1,1]]
for i in range(2,num):
    last = lis[-1]
    res = []
    j = 0
    while j < len(last)-1:
        #print(j)
        count = 1
        k = j+1
        while k < len(last) and last[j]==last[k]:
            #print(j , " " ,k)
            count+=1
            k+=1
        res.append(count)
        res.append(last[j])
        j = k
    if last[-1] != last[-2]:
        res.append(1)
        res.append(last[-1])
        
        
    lis.append(res)

for i in lis:
    i = [str(j) for j in i ]
    print(' '.join(i))
    
