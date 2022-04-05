# Задание 3

cube_list = [pow(i, 3) for i in range(1, 1000, 2)]
sum = 0
result_list = []
i = 0
while i < len(cube_list):
    cub = cube_list[i]
    i += 1
    sum_n = 0
    tmp = cub
    while tmp > 0:
        sum_n += tmp % 10
        tmp //= 10
    if sum_n % 7 == 0:
        print(f'{cub}, {sum_n}')
        result_list.append(cub)
for n in result_list:
    sum += n
print(sum)
