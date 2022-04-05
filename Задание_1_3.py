#Задание 3

proc = int(input('Введите количество процентов: '))
if proc == 1:
    print(f'{proc} процент')
elif 1 < proc < 5:
    print(f'{proc} процента')
elif 4 < proc < 21:
    print(f'{proc} процентов')