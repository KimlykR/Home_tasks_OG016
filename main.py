# Калькулятор через функцию
what = input("Что делаем? (+,-,*, :):")
a = float(input("Введи первое число:"))
b = float(input("Введи второе число:"))


def add(a, b,):
    if what == "+":
        return a+b
    elif what == "-":
        return a-b
    elif what == ":":
        return a/b
    elif what == "*":
        return a*b
    else :
        print("Эрор!!1")


print("Результат:" + str(add(a,b)))