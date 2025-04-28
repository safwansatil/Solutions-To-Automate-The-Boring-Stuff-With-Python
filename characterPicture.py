#The trick was that you just transpose the matrix
import copy as copy
grid = [
['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']
]
def printTranspose(grid):
    copyGrid = copy.deepcopy(grid) #does nothing
    numRows = len(grid)
    numCols = len(grid[0])
    for i in range(numCols):
        for j in range(numRows):
            print(grid[j][i], end='')
        print()
printTranspose(grid)