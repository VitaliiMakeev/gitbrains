def thesaurus_adv(names: list):
    name_dict = {}
    for name in names:
        first_name = name.split()[0]
        second_name = name.split()[1]
        letter_fn = first_name[0]
        letter_sn = second_name[0]
        if name_dict.get(letter_sn) is None:
            name_dict[letter_sn] = {letter_fn: name}
        else:
            if name_dict.get(letter_sn) is not None:
                if name_dict[letter_sn].get(letter_fn):
                    name_dict[letter_sn].update({letter_fn: [*name_dict[letter_sn].values(), name]})
                else:
                    name_dict[letter_sn].update({letter_fn: [name]})
    for key in sorted(name_dict.keys()):
        print(key, ':', name_dict[key])
    print(f'\n{name_dict}')

name_full_list = ['Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Геннадий Васильев']
thesaurus_adv(name_full_list)