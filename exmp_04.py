# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

import random

def sum_numbers(list_num):
    """Находим сумму цифр числа"""
    even_sum = []
    for i in range(0, len(list_num)-1):
        sum_digit = 0
        numbers = str(list_num[i])
        numbers = [int(digit) for digit in numbers]
        sum_digit = sum(numbers)
        if sum_digit % 2 == 0:
            even_sum.append(list_num[i])
    return even_sum

list_numbers = [random.randint(1,100) for i in range(1,10)]
print(f'                    Исходный список: {list_numbers}')
list_even_sum = sum_numbers(list_numbers)
print(f'Список чисел с четными суммами цифр: {list_even_sum}')
