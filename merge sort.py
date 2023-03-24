def merge(a,b):
    final_res = []
    a_ind , b_ind = 0 , 0
    while a_ind < len(a) and b_ind < len(b) :
        if a[a_ind] < b[b_ind]:
            final_res.append(a[a_ind])
            a_ind += 1
        else:
            final_res.append(b[b_ind])
            b_ind += 1
    if a_ind == len(a):
        final_res.extend(b[b_ind : ])
    else:
        final_res.extend(a[a_ind : ])
    print(final_res)
    return final_res

def merge_sort(a):
    if len(a)<=1:
        return a
    left , right = merge_sort(a[: int(len(a)/2)]) , merge_sort(a[int(len(a)/2) : ])
    print(left , " ", right)
    return merge(left,right)

array = input("Enter the array elements : ").split()
array = [int(i) for i in array]
print("\n\n", merge_sort(array))
