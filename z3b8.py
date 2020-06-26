def SynchronizingTables(N, ids, salary):
    def findFirstNull(dictionary):
        for key in dictionary:
            if (dictionary[key] == 0):
                return key
    index = 0
    listSize = len(salary)
    matchDict = {}
    sortedSalaries = sorted(salary)
    for el in ids:
        matchDict[el] = 0
    while index < listSize:
        minId = findFirstNull(matchDict)
        for key in matchDict:
            if (key <= minId) & (matchDict[key] == 0):
                matchDict[key] = sortedSalaries[index]
                if key != minId:
                    matchDict[minId] = 0
                    minId = key
        index += 1

    result = []

    for value in matchDict.values():
        result.append(value)

    return result
