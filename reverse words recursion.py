res = []
def reverse_rec(string_list):
    if string_list !=[]:
        res.append(string_list[-1])
        reverse_rec(string_list[:-1])
        
inp = input("enter the string : ").split()
reverse_rec(inp)
print('Reversed string is : ', ' '.join(res))
