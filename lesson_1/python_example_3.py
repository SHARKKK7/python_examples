# №3 Вывести на экран числа от -N до N.
import os
import string


def clear():
    return os.system('cls')
clear()

def read_num():
    return int(input("Введите число N: "))

def print_n():
    result = ""
    for i in range(-n, n):
        result += str(i)
        result += ", "
    result += str(n)
    return result

n = read_num()
result = print_n()
print(result)
