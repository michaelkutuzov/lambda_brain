def squirrel(N):
    def factorial(N):
        counter = 1
        result = 1
        while counter <= N:
            result = result * counter
            counter += 1
        return result

    f = factorial(N)
    return int(str(f)[0])
