SPACE = ' '


def SplitString(l, s):
    counter = 0
    strLength = len(s)
    parts = []
    prev_delimiter = 0
    current_delimiter = 0
    for i in range(strLength):
        if (s[i] == SPACE):
            current_delimiter = i
        if (counter == l):
            if (current_delimiter == 0):
                current_delimiter = i
                parts.append(s[prev_delimiter:current_delimiter])
                prev_delimiter = current_delimiter
                counter = i - current_delimiter
            else:
                parts.append(s[prev_delimiter:current_delimiter])
                prev_delimiter = current_delimiter + 1
                counter = i - current_delimiter - 1
            current_delimiter = 0
        if (i == strLength - 1):
            parts.append(s[prev_delimiter:])
            break
        counter += 1

    return parts


def FindWord(s, word):
    words = s.split(SPACE)
    res = 0
    for w in words:
        if w == word:
            res += 1

    return res


def WordSearch(len, s, subs):
    strArray = SplitString(len, s)
    numArray = []
    for string in strArray:
        numArray.append(FindWord(string, subs))

    return numArray
