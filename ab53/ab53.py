from math import sqrt, ceil


def encode_s(s):
    encoded_s = ''
    s_with_no_spaces = s.replace(' ', '')
    step = ceil(sqrt(len(s_with_no_spaces)))
    for j in range(0, step):
        i = j
        while i < len(s_with_no_spaces):
            encoded_s = encoded_s + s_with_no_spaces[i]
            i += step
        if j != step - 1:
            encoded_s = encoded_s + ' '
    return encoded_s


def decode_s(s):
    arr = s.split(' ')
    decoded_s = ''
    for j in range(0, len(arr[0])):
        for word in arr:
            if len(word) > j:
                decoded_s = decoded_s + word[j]
    return decoded_s


def TheRabbitsFoot(s, encode):
    if encode:
        return encode_s(s)

    return decode_s(s)
