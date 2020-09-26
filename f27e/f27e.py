def find_min_greatest_num(str):
    min_greater_num = 0
    for index, char in enumerate(str):
        if ord(char) > ord(str[0]):
            if min_greater_num == 0:
                min_greater_num = index
            else:
                if ord(char) < ord(str[min_greater_num]):
                    min_greater_num = index

    return min_greater_num


def switch_letters(str, ind_1, ind_2):
    new_str = ''
    for i in range(0, len(str)):
        if i == ind_1:
            new_str += str[ind_2]
        elif i == ind_2:
            new_str += str[ind_1]
        else:
            new_str += str[i]

    return new_str


def check_asc(str):
    if len(str) == 1:
        return True

    for i in range(1, len(str)):
        if str[i] < str[i - 1]:
            return False

    return True


def BiggerGreater(input):
    greater_input = input
    min_greater_num = find_min_greatest_num(input)

    if min_greater_num:
        greater_input = switch_letters(greater_input, 0, min_greater_num)
        if not check_asc(greater_input[1:]):
            print('greater_input', greater_input, 2)
            greater_input = greater_input[0] + \
                ''.join(sorted(greater_input[1:]))
    else:
        if check_asc(greater_input[1:]):
            greater_input = switch_letters(
                greater_input, len(greater_input) - 1, len(greater_input) - 2)
            print('greater_input', greater_input, 3)
        else:
            print('greater_input', greater_input, 4)
            greater_input = greater_input[0] + BiggerGreater(greater_input[1:])

    print('greater_input', greater_input, 5)
    if greater_input == input:
        return ''
    else:
        return greater_input
