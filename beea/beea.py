STEP = 3


def sort_desc(array):
    sorted_arr = sorted(array, reverse=True)
    return sorted_arr


def MaximumDiscount(N, price):
    i = 2
    discount = 0
    sorted_price = sort_desc(price)

    while i <= N - 1:
        print('discount', discount)
        discount += sorted_price[i]
        i += STEP

    return discount
