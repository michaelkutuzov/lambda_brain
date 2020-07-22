ASTERISK = "*"


def get_period(line):
    for i in range(1, len(line)):
        if line[i] == ASTERISK:
            return i


def LineAnalysis(line):
    L = len(line)
    if (L == 1) & (line[0] == ASTERISK):
        return True
    if (line[0] != ASTERISK) | (line[-1] != ASTERISK):
        return False

    period = get_period(line)
    i = 0
    while i < L:
        if line[i] != ASTERISK:
            return False
        i += period

    return True
