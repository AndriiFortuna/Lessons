# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

    if month == 1:
        print('Вы ввели', month, "месяц, в нем 31 день")
    elif month == 2:
        print('Вы ввели', month, "месяц, в нем 28 дней")
    elif month == 3:
        print('Вы ввели', month, "месяц, в нем 31 день")
    elif month == 4:
        print('Вы ввели', month, "месяц, в нем 30 дней")
    elif month == 5:
        print('Вы ввели', month, "месяц, в нем 31 день")
    else:
        print("Номер месяца введен некоректно")

