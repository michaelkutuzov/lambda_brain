def sum_array(array):
    summ = 0
    for elem in array:
        summ += elem

    return summ


def MassVote(N, Votes):
    part = 0.0
    counter = 0
    index = 0

    summ = sum_array(Votes)

    for i, vote in enumerate(Votes, start=1):
        p = float(round(vote / summ, 3))
        print('percent', p)
        if p > 0.5:
            return 'majority winner ' + str(i)
        elif p > part:
            part = p
            counter = 1
            index = i
        elif p == part:
            counter += 1

    if counter > 1:
        return 'no winner'
    else:
        return 'minority winner ' + str(index)
