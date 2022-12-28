# 4-Создайте два списка — один с названиями языков программирования, 
# другой — с их нумерацией. ['python', 'c#'] и  [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей,
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — 
# которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, 
# его номер заменяется на сумму очков.
# [сумма очков C# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. 
# Суммой очков называется сложение порядковых номеров букв в слове. 
# Cложите получившиеся числа и верните из функции в качестве ответа 
# вместе с преобразованным списком

def upp_char(languages):
    """Переводим буквы из строчных в заглавные"""
    upp_languages = list(map(str.upper, languages))
    return upp_languages
 
def list_num_lang(list1, list2):
    """Создаем кореж из двух списков"""
    data = list(zip(list1, list2))
    return data

def sum_word(word):
    """Находим сумму очков слова"""
    sum_code = 0
    for ch in range(0,len(word)):
        sum_code += ord(word[ch])
    print(f'\nСумма очков слова {word} составляет {sum_code}')
    return sum_code
    
def factors_calculation(number):
    """Создает список простых множителей заданного числа"""
    factor = 2
    factors_array = []
    while factor * factor <= number:
        if number % factor == 0:
            factors_array.append(factor)
            number //= factor
        else:
            factor += 1
    if number > 1:
        factors_array.append(number)
    return factors_array
   
def string_search(list_searched, chars_desired):
    """Считаем количество вхождений искомых символов в список"""
    if list_searched.count(chars_desired) > 0:
        return list_searched.count(chars_desired)


program_lang = ['python', 'c#']
numbers = [1, 2]
list_del_element = []
list_sum_word = []
languages = upp_char(program_lang)
enumer_lang = list_num_lang(numbers, languages)
print(f'Создали кортеж номер + язык: {enumer_lang}')

for l in enumer_lang:
    x = list(tuple(l))
    for n in range(0, len(enumer_lang)-1):
        sum_lang = sum_word(x[1]) 
        list_sum_word.append(sum_lang)
        factor_language = factors_calculation(sum_lang)
        num_lang_entry = factor_language.count(x[0])

        if num_lang_entry == 0:
            list_del_element.append(n)

list_sum_word_lang = list_num_lang(list_sum_word, languages)
print(f'\nCписок языков с суммой очков из названия: {list_sum_word_lang}')

for i in range(0, len(list_del_element)):
    d = list_del_element[i]
    if i == d: del list_sum_word_lang[i]
print(f'\nВыводим итоговый список: {list_sum_word_lang}')
    

