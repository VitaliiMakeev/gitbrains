def convert_time(duration: int) -> str:
    if duration < 0:
        return 'Вы ввели отрицательное время'
    elif duration < 60:
        return f'{duration} сек'
    elif duration < 3600:
        return f'{duration // 60} мин, {duration % 60} сек'
    elif duration < 86400:
        return f'{duration // 3600} час, {(duration % 3600) // 60} мин {(duration % 3600) % 60} сек'
    elif duration < 2592000:
        return f'{duration // 86400} дней, {(duration % 86400) // 3600} час {((duration % 86400) % 3600) // 60} мин, {((duration % 86400) % 3600) % 60} сек'


duration = 1000000
result = convert_time(duration)
print(result)