# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def string_search(list_searched, chars_desired):
    """Считаем количество вхождений искомых символов в список"""
    print(f'\nВ списке {list_searched} ищем {chars_desired}.\nРезультат: ', end = ' ')
    if list_searched.count(chars_desired) > 1:
        print(list_searched.count(chars_desired))
    else: print(-1)

list1 = ['qwe', 'asd', 'xc', 'qwe', 'ertqwe']
find_char1 = 'qwe'
list2 = ['йцу', 'фыв', 'ячс', 'цук', 'йцукен', 'йцу']
find_char2 = 'йцу'
list3 = ['йцу', 'фыв', 'ячс', 'цук', 'йцукен']
find_char3 = 'йцу'
list4 = ['123', '234', 123, '567']
find_char4 = '123'
list5 = []
find_char5 = '123'

string_search(list1, find_char1)
string_search(list2, find_char2)
string_search(list3, find_char3)
string_search(list4, find_char4)
string_search(list5, find_char5)