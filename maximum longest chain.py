# its looks like a activity selection problem in algorithms

arr=[[5,9],[3,7],[8,10],[11,16],[18,20]]
n = len(arr)
for i in range(0,n):
    for j in range(0,n):
        if arr[i][1]<arr[j][1] and i!=j:
            arr[i] ,arr[j] = arr[j] ,arr[i]
#print(arr)
max_len = 1
i=0
print(arr[i],end=',')
for j in range(1,n):
    if arr[i][1]<arr[j][0]:
        print(arr[j],end=',')
        i=j
        
            
