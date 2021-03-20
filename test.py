sudokuGrid = [
            0, 0, 1, 0, 4, 0, 6, 0, 0,
            2, 0, 0, 0, 0, 0, 0, 3, 5,
            0, 0, 0, 0, 0, 0, 9, 0, 0,
            0, 0, 0, 0, 5, 0, 0, 0, 0,
            8, 3, 0, 0, 0, 0, 4, 0, 7,
            6, 0, 0, 8, 0, 0, 0, 0, 9,
            0, 0, 0, 5, 6, 1, 0, 0, 2,
            0, 0, 0, 0, 0, 0, 1, 0, 0,
            5, 0, 7, 0, 0, 2, 0, 0, 0,
]

def solver(currentGrid, zeroIndex, trialVal):
    # set up trial grid
    trialGrid = currentGrid.copy()
    trialGrid[zeroIndex] = trialVal

    if checkGridGood(trialGrid) == False:
        return currentGrid
    
    if 0 not in trialGrid:
        return trialGrid

    # trial grid is good
    nextInd = getNextZero(trialGrid)

    for i in range(9):
        returnedGrid = solver(trialGrid, nextInd, i+1)
        if returnedGrid != trialGrid:
            #isGoodForIteration
            return returnedGrid
        if (i == 8):
            #exhausted all trials
            return currentGrid

def getNextZero(grid):
    if 0 in grid:
        return grid.index(0)
        
def checkNines(boxLine):
    count = [0] * 9

    for i in range(9):
        num = boxLine[i]
        if num != 0:
            count[num - 1] += 1

    if max(count) >= 2:
        return False
    
    return True

def checkGridGood(grid):
    for i in range(9):
        if not checkNines(grid[i*9:9*(i+1)]):
            # checkHorzontalLines
            return False
        if not checkNines(grid[i::9]):
            # checkVerticalLines
            return False
    
    for i in range(3):
        for j in range(3):
            box = []
            yShift = i*9*3
            box = box + grid[j*3 +yShift:3*9+j+yShift:9]
            box = box + grid[j*3+1+yShift:3*9+j+1+yShift:9]
            box = box + grid[j*3+2+yShift:3*9+j+2+yShift:9]
            # print(box)
            if not checkNines(box):
                return False

    return True

def displayGrid(grid):
    for i in range(81):
        if (i % 9 == 0):
            print(" ")
        print(grid[i], end=" ")
        
#solve grid
for i in range(9):
    print('Trialing', end=" ")
    print(i+1)
    solvedGrid = solver(sudokuGrid, getNextZero(sudokuGrid), i+1)
    
    if (solvedGrid != sudokuGrid):
        print(' ')
        print('Solution Found!')
        displayGrid(solvedGrid)
        break
    else:
        print('--- no solution found ---')
    
    if i==8:
        #can not be solved
        print('Grid cannot be solved!')