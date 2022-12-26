# 2- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

numbers = [2, 3, 4, 5, 6]
numbers1 = [2, 3, 5, 6]

def output_pair(element, first, second):
    """Выводит на консоль пару перемножаемых чисел"""
    print(f'Пара', element+1, ':', first, '-', second)

def product_calcilation(list_digit):
    """Возвращает произведение двух чисел"""
    l = len(list_digit)//2 + 1 if len(list_digit) % 2 != 0 else len(list_digit)//2
    calcilation = [list_digit[i]*list_digit[len(list_digit)-i-1] for i in range(l)]
    print(f'\nПеремножаем пары в списке {list_digit}. Результат: {calcilation}\n')

product_calcilation(numbers)
product_calcilation(numbers1)
