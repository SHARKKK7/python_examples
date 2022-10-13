# № 4
import os 

def clear():
    return os.system('cls')
clear()


# round_num = int(num)
# result = (num - round_num)*10

def first_float():
    n = input("Введите вещественное число: ")
    n_list = n.split('.')
    print(n_list[1][0])

first_float()