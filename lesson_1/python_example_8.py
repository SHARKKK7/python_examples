# №8 Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.
import os

def clear():
    return os.system('cls')
clear()

a = int(input("введите кординаты X: "))
b = int(input("введите кординаты Y: "))

if a > 0 and b > 0:
    print("1 четверть")
elif a < 0 and b < 0:
    print("3 четверть")
elif a > 0 and b < 0:
    print("4 четверть")
elif a < 0 and b > 0:
    print("2 четверть")
else:
    print("Вы на кординатных осях")
