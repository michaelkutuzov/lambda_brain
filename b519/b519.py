def ShopOLAP(N, items):
    sell_data = {}
    reverse_sell_data = {}
    for item in items:
        item_data = item.split(' ')
        product = item_data[0]
        quantity = item_data[1]

        if product in sell_data:
            sell_data[product] = int(sell_data[product]) + int(quantity)
        else:
            sell_data[product] = int(quantity)

    list_sell_data = list(sell_data.items())
    for el in list_sell_data:
        product = el[0]
        quantity = el[1]
        if quantity in reverse_sell_data:
            reverse_sell_data[quantity].append(product)
        else:
            reverse_sell_data[quantity] = [str(product)]

    reverse_sell_data_keys_list = list(reverse_sell_data.keys())
    reverse_sell_data_keys_list.sort(reverse=True)

    result = []
    for quantity in reverse_sell_data_keys_list:
        for product in sorted(reverse_sell_data[quantity]):
            result.append(f'{product} {quantity}')

    return result
