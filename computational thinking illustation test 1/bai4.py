row=int(input())
matrix=[]
for k in range(row):
    a=list(map(int,input().split()))
    matrix.append(a)

def count_local_peaks(matrix):
    row=len(matrix)
    collum=len(matrix[0])
    count=0
    if row <3 or collum<3:
        return 0
    for r in range(1,row-1):
        for c in range(1,collum-1):
            if matrix[r][c] > matrix[r-1][c] and matrix[r][c] > matrix[r+1][c] and matrix[r][c] > matrix[r][c-1] and matrix[r][c] > matrix[r][c+1]:
                count+=1
    return count

print(count_local_peaks(matrix))

    