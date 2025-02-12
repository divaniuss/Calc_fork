from math import *
import os

HISTORY_FILE = "history.txt"

# Создание файла истории, если его нет
if not os.path.exists(HISTORY_FILE):
    open(HISTORY_FILE, "w").close()

lang = "eng"
shure = "n"
con = "y"
num1 = 0
changeLang = "Change language (kz/rus/eng) or to exit enter exit: "
langerror = "Error: Invalid language"

while shure == "n":
    lang = input(changeLang)

    if lang == "eng":
        changeLang = "Change language (kz/rus/eng) or to exit enter exit: "
        num1word = "Enter first number: "
        num2word = "Enter second number: "
        opword = "Enter operation (+, -, *, /, ^, sqr, history): "
        sumword = "Sum: "
        diffword = "Difference: "
        prodword = "Product: "
        quotword = "Quotient: "
        powword = "Power: "
        sqrtword = "Square root: "
        shureword = "Are you sure? (y/n): "
        conword = "Continue? (y/n): "
        zeroerror = "Error: Division by zero"
        langerror = "Error: Invalid language"
        operror = "Error: Enter correct operation"
    elif lang == "rus":
        changeLang = "Изменить язык (kz/rus/eng) или чтобы выйти введите exit: "
        num1word = "Введите первое число: "
        num2word = "Введите второе число: "
        opword = "Введите операцию (+, -, *, /, ^, sqr, history): "
        sumword = "Сумма: "
        diffword = "Разность: "
        prodword = "Произведение: "
        quotword = "Частное: "
        powword = "Степень: "
        sqrtword = "Квадратный корень: "
        shureword = "Вы уверены? (y/n): "
        conword = "Продолжить? (y/n): "
        zeroerror = "Ошибка: Деление на ноль"
        langerror = "Ошибка: Неверный язык"
        operror = "Ошибка: Введите правильную операцию"
    elif lang == "kz":
        changeLang = "Тілді өзгерту (kz/rus/eng) немесе шығу үшін exit жазыңыз: "
        num1word = "Бірінші санды енгізіңіз: "
        num2word = "Екінші санды енгізіңіз: "
        opword = "Операцияны енгізіңіз (+, -, *, /, ^, sqr, history): "
        sumword = "Қосынды: "
        diffword = "Айырмашылық: "
        prodword = "Көбейту: "
        quotword = "Бөліну: "
        powword = "Дәрежесі: "
        sqrtword = "Квадрат түбірі: "
        shureword = "Сіз сенімдісіз бе? (y/n): "
        conword = "Жалғастыру? (y/n): "
        zeroerror = "Қате: Нольға бөлу"
        langerror = "Қате: Дұрыс тілді таңдаңыз"
        operror = "Қате: Дұрыс операция енгізіңіз"
    elif lang == "exit":
        exit()

    if lang not in ["kz", "rus", "eng"]:
        print(langerror)
        continue
    shure = input(shureword)

while con == "y":
    op = input(opword)
    result_str = ""

    if op == "history":
        with open(HISTORY_FILE, "r") as file:
            history = file.read()
        print(history if history else "История пуста.")
        continue
    elif op == "sqr":
        num1 = float(input(num1word))
    else:
        num1 = float(input(num1word))
        num2 = float(input(num2word))

    match op:
        case "+":
            result = num1 + num2
            result_str = f"{num1} + {num2} = {result}"
        case "-":
            result = num1 - num2
            result_str = f"{num1} - {num2} = {result}"
        case "*":
            result = num1 * num2
            result_str = f"{num1} * {num2} = {result}"
        case "/":
            if num2 == 0:
                print(zeroerror)
                continue
            result = num1 / num2
            result_str = f"{num1} / {num2} = {result}"
        case "^":
            result = pow(num1, num2)
            result_str = f"{num1} ^ {num2} = {result}"
        case "sqr":
            result = sqrt(num1)
            result_str = f"√{num1} = {result}"
        case _:
            print(operror)
            continue

    print(result_str)

    with open(HISTORY_FILE, "a") as file:
        file.write(result_str + "\n")

    con = input(conword)