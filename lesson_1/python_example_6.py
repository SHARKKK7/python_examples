# №6 Найти максимальное из 5 чисел.
import os


def clear(): 
    return os.system('cls')
clear()

def check_day_of_week(day):
    text = " "
    if day == 1:
        text = "Понедельник"
    elif day == 2:
        text = "Вторник"
    elif day == 3:
        text = "Среда"
    elif day == 4:
        text = "Четверг"
    elif day == 5:
        text = "Пятница"
    elif day == 6:
        text = "Суббота"
    elif day == 7:
        text = "Воскресенье"
    else:
        text = "Не корректные данные"

    if day == 6 or day == 7:
        text += " выходной день" 
    return text

day = int(input("Введите номер дня недели: "))
print(check_day_of_week(day))