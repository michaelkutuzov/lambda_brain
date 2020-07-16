def col_form_minus(pair):
    def get_next_digit(int_str, index):
        if index < -len(int_str):
            return ''
        else:
            return int(int_str[index])

    def remove_nulls(int_str):
        res = 0
        li = len(int_str)
        for i in range(li):
            if int_str[i] == '0':
                res += 1
            else:
                break

        if res == li:
            return '0'
        else:
            return int_str[res:li]
    minuend = pair[0]
    subtrahend = pair[1]
    lm = len(minuend)
    ls = len(subtrahend)
    result = ''
    next_digit = int(minuend[-1])

    for i in range(1, ls + 1):
        s = int(subtrahend[-i])

        if next_digit >= s:
            result = str(next_digit - s) + result
            next_digit = get_next_digit(minuend, -(i + 1))
        else:
            result = str(next_digit - s + 10) + result
            next_digit = get_next_digit(minuend, -(i + 1)) - 1

    result = str(next_digit) + result

    if lm > ls + 1:
        print(lm, ls)
        for j in range(ls + 2, lm + 1):
            print(minuend[-j])
            result = minuend[-j] + result

    return remove_nulls(result)


def check_for_equality(s1, s2):
    for i in range(0, len(s1)):
        if (s1[i] > s2[i]):
            return (s1, s2)
        elif (s1[i] < s2[i]):
            return (s2, s1)
        else:
            continue
    return ('0', '0')


def BigMinus(s1, s2):
    str_tuple = ()
    if len(s2) > len(s1):
        str_tuple = (s2, s1)
    elif len(s1) > len(s2):
        str_tuple = (s1, s2)
    else:
        str_tuple = check_for_equality(s1, s2)

    if str_tuple == ('0', '0'):
        return '0'

    return col_form_minus(str_tuple)
