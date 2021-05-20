import random


def lol():
    min = int(input("Введите минимальное число:"))
    max = int(input("Введите максимальное число:"))
    quantity = int(input("Введите количество генерируемых чисел:"))
    return [random.randint(min,max) for i in range (quantity)]


def lol2():
    min2 = int(input("Введите минимальное число:"))
    max2 = int(input("Введите максимальное число:"))
    quantity2 = int(input("Введите количество генерируемых чисел:"))
    return [random.randint(min2,max2) for i in range (quantity2)]


a =(lol())
print(a)
b = (lol2())
print(b)
c = list(set(a)^set(b))
print('Уникальные числа:', c)