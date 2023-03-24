def spiral_pattern(matrix,n):
    top = 0
    bot = n-1
    left = 0
    right = n-1
    direction = 0 
    pat = n
    while top <= bot and left <= right:
        if direction == 0:   # top left -> top right way
            for i in range(left , right+1):
                matrix[top][i]=pat
            top+=1
            direction = 1
            
        elif direction == 1:   # top right -> bottom right way
            for i in range(top , bot+1):
                matrix[i][right]=pat
            right-=1
            direction = 2

        elif direction == 2:   # bottom right -> bottom left way
            for i in range(right , left-1 , -1):
                matrix[bot][i]=pat
            bot-=1
            direction = 3

        elif direction == 3:   # bottom left -> top left way
            for i in range(bot , top-1 , -1):
                matrix[i][left]=pat
            left+=1
            direction = 0
            pat-=1   
    return matrix

n = int(input(" Enter the n : "))
matrix=[]
for i in range(n):
    temp = [0 for j in range(n)]
    matrix.append(temp)
spiral = spiral_pattern(matrix,n)
print("The Spiral Pattern is")
for i in spiral:
    i = [ str(j) for j in i ]
    print(' '.join(i))

