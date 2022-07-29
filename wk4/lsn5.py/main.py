def register():
    # name = input('enter name')
    # surname = input('enter surname')
    # age = int(input('enter age'))
    # lang = input('enter your programm language:')
    dict = {
        'name': 'y',
        'surname': 'e',
        'age': 13,
        'lang': 'py',
    }
    return dict

def save_at_file(dict1: dict):
    with open('resolt.txt', 'w') as f:
        for k in dict1.items():
            f.write(f'{k} \n')
    print('done')

save_at_file(register())