# №5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30
import os

def clear():
    return os.system('cls')
clear()

num = input("Введите число: ")

def find(num):
    if num%30 !=0:
        if num%5==0 and num%10==0 or num%15==0:
            print("Число ....")