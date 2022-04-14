def num_translate_adv(value: str) -> str:
    numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
               'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if value[0].isupper():
        str_out = numbers[value.lower()].title()
    else:
        str_out = numbers[value]
    return str_out


print(num_translate_adv('One'))
print(num_translate_adv('eight'))

