#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def list_rand_number(count: int):
    if count < 0:
        print("Отрицательное значение!")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def sum_pos(list_nums: list):
    result = 0
    for k in range(0, len(list_nums), 2):
        result += list_nums[k]
    return result

all_list = list_rand_number(int(input("Введите кол-во элементов: ")))
print(all_list)
print(sum_pos(all_list))