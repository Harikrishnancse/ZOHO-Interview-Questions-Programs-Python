def spiral_matrix(matrix,m,n):
    top = 0
    bot = m-1
    left = 0
    right = n-1
    direction = 0
    spiral = []
    
    while top <= bot and left <= right:
        if direction == 0:   # top left -> top right way
            for i in range(left , right+1):
                spiral.append(matrix[top][i])
            top+=1
            direction = 1
            
        elif direction == 1:   # top right -> bottom right way
            for i in range(top , bot+1):
                spiral.append(matrix[i][right])
            right-=1
            direction = 2

        elif direction == 2:   # bottom right -> bottom left way
            for i in range(right , left-1 , -1):
                spiral.append(matrix[bot][i])
            bot-=1
            direction = 4

        elif direction == 4:   # bottom left -> top left way
            for i in range(bot , top-1 , -1):
                spiral.append(matrix[i][left])
            left+=1
            direction = 0

    return spiral


r,c = map(int,input(" Enter the m,n : ").split())
matrix=[]
print(" Enter the matrix elements row wise only ")
for i in range(r):
    temp = input().split()
    matrix.append(temp)
#print(matrix)
spiral = spiral_matrix(matrix,r,c)
print("Spiral Matrix is : ", ' '.join(spiral))

