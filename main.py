# Калькулятор через функцию
what = input("Что делаем? (+,-,*, :):")
a = float(input("Введи первое число:"))
b = float(input("Введи второе число:"))

if what == "+":
    с = a + b
    print("Результат:" + str(с))
elif what == "-":
    с = a - b
    print("Результат:" + str(с))
elif what == "*":
    c = a * b
    print("Результат:" + str(c))
elif what == ":":
    c = a / b
    print("Результат:" + str(c))
else:
    print("Ошибка ввода")
