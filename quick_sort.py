def quick_sort(a):
    if len(a) <= 1:
        return a
    smaller , larger = [],[]
    pivot , i , j = 0 , 0 , len(a)-1
    while(i<j):
        if a[i] <= a[pivot]:
            i+=1
        elif a[j] > a[pivot]:
            j-=1
        if i<=j:
            a[i],a[j] = a[j],a[i]
    pivot , j = j , pivot
    smaller.append( quick_sort( a[ : pivot+1 ] ))
    larger.append( quick_sort( a[ pivot :  ] ))
    return smaller+larger

array = input("Enter the array : ").split()
array = [int(i) for i in array]
print(quick_sort(array))
        
                           
                            
    
    
    
