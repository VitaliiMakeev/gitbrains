def sum_list_1(dataset: list) -> int:
    summa_numbers = 0
    for i in range(1, 1000, 2):
        summa = 0
        m = i ** 3 + 17
        a = m
        while m > 0:
            summa += m % 10
            m //= 10
        if summa % 7 == 0:
            summa_numbers += a
    return summa_numbers


my_list = []
result_1 = sum_list_1(my_list)
print(result_1)