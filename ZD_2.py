def convert_list_in_str(list_in: list) -> str:
    new_list = []
    str_out = ''
    for word in list_in:
        if word.isdigit():
            new_list.extend(['"', word.zfill(2), '"'])
            str_out += f'"{word.zfill(2)}"'
        elif word[0] == '+' or word[0] == '-':
            if len(word) == 2:
                new_list.extend(['"', f'{word[0]}0{word[1:]}', '"'])
                str_out += f'"{word[0]}0{word[1:]}"'
            else:
                new_list.extend(['"', word, '"'])
                str_out += f'"{word}"'
        else:
            new_list.append(word)
            str_out += f' {word} '
    return str_out



my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)