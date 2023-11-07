def num_check(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


print("Вас приветствует Калькулятор. Вы знаете как им пользоваться?")
print("1 - Да")
print("2 - Нет")
skill_query = input()
while skill_query != "1" and skill_query != "2":
    print("Введите 1 либо 2")
    skill_query = input()
if skill_query == "2":
    print("Вводится первое число х, мат. символ, второе число у.\n")
    print("Операции:\n")
    print("+ -  сложение,\n" +
          "- - вычитание,\n" +
          "* - умножение,\n" +
          "/ - деление,\n" +
          "// - целочисленное деление,\n" +
          "% извлекание остатка от деления,\n" +
          "** - возведение в степень,\n" +
          "*/ - корень числа Y степени 1/х,\n" +
          ">> - перевод в десят. систему счисления, где у - осн. системы\n" +
          "? - анализ числа, где у - пункт анализа, кот. нужно выполнить" +
          "(!= 7 - выполнить все пункты).\n")
    
operators = ["+", "-", "*", "/", "//", "%", "**", "*/", ">>", "?"]
start_query = "1"
while start_query == "1":  
    x = input()
    sign = input()
    y = input()
    while not num_check(x) or sign not in operators or not num_check(y):
        print("Введите пример заново, не нарушая правил.")
        x = input()
        sign = input()
        y = input()
    if "." not in x:
        x = int(x)
    else:
        x = float(x)
    if "." not in y:
        y = int(y)
    else:
        y = float(y)
    if sign == "+":
        print(x + y)
    elif sign == "-":
        print(x - y)
    elif sign == "*":
        print(x * y)
    elif sign == "/":
        print(x / y)
    elif sign == "//":
        print(x // y)
    elif sign == "%":
        print(x % y)
    elif sign == "**":
        print(x ** y)
    elif sign == "*/":
        print(pow(y, 1/x))
    elif sign == ">>":
        y = int(y)
        x = str(x)
        print(int(x, y))
    elif sign == "?":
        if y == 1:
            if type(x) == int:
                print("Кол-во разрядов - " + str(len(str(x))))
            else:
                print("Кол-во разрядов - " + str(len(str(x)) - 1))
        elif y == 2:
            x = str(x)
            for i in range(10):
                if x.count(str(i)) > 0:
                    print(str(i) + " - " + str(x.count(str(i))))
            x = float(x)
        elif y == 3:
            if x % 2 == 0:
                print("Четное")
            else:
                print("Нечетное")
        elif y == 4:
            c = 0
            x = str(x)
            for i in x:
                if i != ".":
                    c += int(i)
            print("Сумма цифр равна " + str(c))
            x = float(x)
        elif y == 5:
            a = True
            for i in range(1, x + 1):
                if x % i == 0:
                    if x % i != x and x % i != 1:
                        a = False
                    print(str(i) + " - делитель числа " + str(x))
            if a:
                print(str(x) + " - простое число")
        elif y == 6:
            if x ** 0.5 % 1 == 0:
                print(str(x) + " - полный квадрат числа " + str(x ** 0.5))
            else:
                print(str(x) + " не является полным квадратом")
        elif y == 7:
            if pow(x, 1/3) % 1 == 0:
                print(str(x) + " - полный куб числа " + str(pow(x, 1/3)))
            else:
                print(str(x) + " не является полным кубом")
        else:
            print("Кол-во разрядов - " + str(len(str(x))))
            x = str(x)
            for i in range(10):
                if x.count(str(i)) > 0:
                    print(str(i) + " - " + str(x.count(str(i))))
            x = float(x)
            if x % 2 == 0:
                print("Четное")
            else:
                print("Нечетное")
            c = 0
            x = str(x)
            for i in x:
                if i != ".":
                    c += int(i)
            print("Сумма цифр равна " + str(c))
            x = float(x)
            a = True
            for i in range(1, int(x) + 1):
                if x % i == 0:
                    if x % i != x and x % i != 1:
                        a = False
                    print(str(i) + " - делитель числа " + str(x))
            if a:
                print(str(x) + " - простое число")
            if x ** 0.5 % 1 == 0:
                print(str(x) + " - полный квадрат числа " + str(x ** 0.5))
            else:
                print(str(x) + " не является полным квадратом")
            if pow(x, 1/3) % 1 == 0:
                print(str(x) + " - полный куб числа " + str(pow(x, 1/3)))
            else:
                print(str(x) + " не является полным кубом")
    print("Еще раз?\n1 - Да\n2 - Нет")
    start_query = input()
    while start_query != "1" and start_query != "2":
        print("Введите 1 либо 2")
        start_query = input()
