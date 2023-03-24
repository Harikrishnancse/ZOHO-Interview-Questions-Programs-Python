def merge(a,b):
    if len(a)<len(b):
        a , b = b , a
    res = []
    a_ind , b_ind = 0 , 0
    while a_ind < len(a) and b_ind < len(b):
        if a[a_ind] < b[b_ind]:
            if a[a_ind] not in  res:
                res.append(a[a_ind])
            if b[b_ind] not in  res:
                res.append(b[b_ind])
        elif a[a_ind] > b[b_ind]:
            if b[b_ind] not in  res:
                res.append(b[b_ind])
            if a[a_ind] not in  res:
                res.append(a[a_ind])
        elif a[a_ind] == b[b_ind]:
            if a[a_ind] not in  res:
                res.append(a[a_ind])
        a_ind += 1
        b_ind += 1
            
    if a_ind == len(a):
        while b_ind < len(b): 
            if b[b_ind] not in  res:
                res.append(b[b_ind])
            b_ind += 1
    elif b_ind == len(b):
        while a_ind < len(a): 
            if a[a_ind] not in  res:
                res.append(a[a_ind])
            a_ind += 1
        res.extend( a[a_ind : ])
    return res       

arr1 = input("Enter the array 1 elements : ").split()
arr2 = input("Enter the array 2 elements : ").split()
arr1 = [ int(i) for i in arr1 ]
arr2 = [ int(i) for i in arr2 ]
print(merge(arr1,arr2))
    
