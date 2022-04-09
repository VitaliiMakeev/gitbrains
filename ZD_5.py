my_list = [57.80, 46.51, 97.51, 23.41, 68.12, 14.99, 82.60, 22.40, 30.99, 45.20]
new_price = []


for price in sorted(my_list, reverse=True)[0:5]:
    x = int(price // 1)
    y = int((price - x) * 100)
    new_list = '{} руб. {} коп.'.format(x, y)
    new_price.append(new_list)


print(new_price)













