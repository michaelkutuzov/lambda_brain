from decimal import Decimal, ROUND_HALF_UP


def PatternUnlock(N, hits):
    def getDistance(coord1, coord2):
        def sumOfSquares(a, b):
            return (a * a) + (b * b)
        sumOfsq = sumOfSquares(Decimal(
            coord1[0]) - Decimal(coord2[0]), Decimal(coord1[2]) - Decimal(coord2[2]))
        root = sumOfsq ** Decimal('0.5')
        return root
    coordinates = {
        1: '1_2',
        2: '2_2',
        3: '3_2',
        4: '3_1',
        5: '2_1',
        6: '1_1',
        7: '1_3',
        8: '2_3',
        9: '3_3'
    }
    index = 1
    distance = Decimal('0')

    while index < N:
        distance += getDistance(coordinates[hits[index]],
                                coordinates[hits[index - 1]])
        index += 1

    strDist = str(distance.quantize(Decimal('1.00000'), ROUND_HALF_UP))
    result = ''
    for char in strDist:
        if (char != '.') & (char != '0'):
            result += char
    return result
