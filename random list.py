import random


def lol():
    min = int(input("Введите минимальное число:"))
    max = int(input("Введите максимальное число:"))
    quantity = int(input("Введите количество генерируемых чисел:"))
    list = [random.randint(min,max) for i in range (quantity)]
    print (list)


lol()

