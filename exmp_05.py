# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200.
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

import random

list_numbers = [random.randint(1,5) for i in range(1,5)]
print(f'      Исходный список: {list_numbers}')

numbered_list = list(enumerate(list_numbers))
print(f'  Нумерованный список: {numbered_list}')

result = [numbered_list[i] for i in range(len(list_numbers)) if i != list_numbers[i]]
print(f'Результирующий список: {result}')
