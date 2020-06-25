def odometer(oksana):
    time = 0
    result = 0
    index = 1
    sizeOfList = len(oksana)
    while index < sizeOfList:
        if index % 2 != 0:
            result += oksana[index - 1] * (oksana[index] - time)
            time = oksana[index]
        index += 1

    return result
