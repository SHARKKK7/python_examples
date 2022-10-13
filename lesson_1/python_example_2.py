# №2 Найти максимальное из 5 чисел.
import os

def clear():
    return os.system('cls')
clear()

# get_array_of_five():
#     array_a= []
#     for i in range(5):
#         lst.append(random.randint(0,100))

array_a = [32, 8, 6, 124, 88]
i = 0
max = 0
while i < len(array_a):
    if array_a[i] > max:
        max = array_a[i]
    i +=1 

print(max)