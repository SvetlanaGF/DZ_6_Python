# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random

list_numbers = [random.randint(1,10) for i in range(1,10)]
print(f'                 Исходный список: {list_numbers}')

numbered_list = list(enumerate(list_numbers))
print(f'             Нумерованный список: {numbered_list}')

result = [numbered_list[i] for i in range(len(list_numbers)) if i != list_numbers[i]]
print(f'Номер элемента не равен элементу: {result}')

multiple_five = [result[i] for i in range(len(result)) if (sum(result[i]) % 5 == 0 )]
print(f'         Сумма кортежей кратна 5: {multiple_five}')

