а = float(input('Введите переменную "А": '))
б = float(input('Введите переменную "Б":'))
в = float(input('Введите переменную "В":'))


def funk( а, б, в ):
    while а<б:
        print("а=", а,"Это меньше, чем \"Б\". Добавим",в)
        а+=в
    else:
        print("Получилось")


funk(а,б, в)
