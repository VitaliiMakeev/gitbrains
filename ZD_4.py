def convert_name(list_in: list) -> list:
    new_list = []
    for name in list_in:
        new_list.append(f'Привет, {name.split()[-1].title()}!')
    return new_list


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name(my_list)
print(result)