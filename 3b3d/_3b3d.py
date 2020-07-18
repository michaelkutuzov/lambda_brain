def convert(data, system):
    converted_data = []
    for num in data:
        converted_data.append(int(str(num), system))

    return converted_data


def UFO(N, data, octal):
    if octal:
        return convert(data, 8)

    return convert(data, 16)
