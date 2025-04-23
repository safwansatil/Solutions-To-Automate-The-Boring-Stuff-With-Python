def printTable(tableData):
    maxLen = 0
    for row in tableData:
        for item in row:
            lenData = len(item)
            if lenData>maxLen:
                maxLen = lenData
    rowNum = len(tableData)
    colNum = len(tableData[0])
    for i in range(rowNum):
        for j in range(colNum):
            print(tableData[i][j].ljust(maxLen), end=' ')
        print()  
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]  
printTable(tableData)