def ConquestCampaign(N, M, L, battalion):
    def getNeighbors(cell):
        neighbors = []
        x = int(cell.split('_')[0])
        y = int(cell.split('_')[1])
        if x - 1 > 0:
            fc = x - 1
            neighbors.append(f'{fc}_{y}')
        if x + 1 <= N:
            fc = x + 1
            neighbors.append(f'{fc}_{y}')
        if y - 1 > 0:
            sc = y - 1
            neighbors.append(f'{x}_{sc}')
        if y + 1 <= M:
            sc = y + 1
            neighbors.append(f'{x}_{sc}')
        return neighbors
    victoryDay = 1
    if L == M * N:
        return victoryDay

    index = 1
    conqueredCells = {}

    while index <= L * 2:
        key = str(battalion[index - 1]) + '_' + str(battalion[index])
        conqueredCells[key] = False
        index += 2

    newConqueredCells = conqueredCells.copy()
    while len(newConqueredCells) < M * N:
        conqueredCells = newConqueredCells.copy()
        for cell in conqueredCells:
            if conqueredCells[cell] == False:
                neighbors = getNeighbors(cell)
                if neighbors != {}:
                    for neighbor in neighbors:
                        if not neighbor in conqueredCells:
                            newConqueredCells[neighbor] = False
                newConqueredCells[cell] = True
        victoryDay += 1

    return victoryDay
