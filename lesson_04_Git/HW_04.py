"""
1. Написать функцию, вычисляющее значение функции при х = 1.79

"""
from math import sin, cos, exp, log1p, sqrt, pi
from collections import Counter


def crazy_function_01(x):
    if x <= -1:
        raise ValueError("x should be greater than -1")
    y1 = cos(exp(x)) + log1p((1 + x) ** 2)
    y2 = sqrt(exp(cos(x)) + (sin(pi * x)) ** 2)
    y3 = sqrt(1 / x) + cos(x ** 2)
    y = (y1 + y2 + y3) ** sin(x)
    return y


"""
2. Напишите функцию search_substr(subst, st), которая принимает 2 строки и
определяет, имеется ли подстрока subst в строке st. В случае нахождения
подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!». Должно
быть найдено совпадение независимо от регистра обеих строк.
"""


def search_substr_02(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"


"""
3. На основании строки определить 3 наиболее часто встречаемых символа в
ней. Пробелы нужно игнорировать (не учитывать при подсчете). Для простоты
подсчета количества вхождений символов удобно использовать Counter из
модуля collections.
"""


def top_three_char(str):
    str_no_spaces = str.replace(" ", "")
    cnt_dict = Counter(str_no_spaces)

    top_three = cnt_dict.most_common(3)
    for char, cnt in top_three:
        print(f"The character '{char}' appears {cnt} times.")
    return top_three


"""
4. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется
создать словарь, который в качестве ключей будет принимать данные числа (т.
е. ключи будут типом int), а в качестве значений – количество этих чисел в
имеющейся последовательности. Для построения словаря создайте функцию
count_it(sequence), принимающую строку из цифр. Функция должна
возвратить словарь из 3-х самых часто встречаемых чисел.
"""


def count_it(sequence):
    top_three = top_three_char(sequence)
    # num_list = [int(char) for char in sequence]
    # cnt_dict = Counter(num_list)
    # top_three = cnt_dict.most_common(3)
    top_three_dict = {int(num): count for num, count in top_three}
    return top_three_dict


"""
5. Шахматы. у вас есть стандартное поле 8*8, после введения координат (a, b)
нахождения вашей фигуры и фигуры соперника (с, d), необходимо получить
ответ, угрожает ли вражеская фигура вам
1) вражеская фигура ферзь
2) вражеская фигура конь
"""


def play_chess(a, b, c, d):
    # a == c (горизонталь)
    # b == d (вертикаль)
    # abs(a - c) == abs(b - d) (диагональ)
    is_queen = (a == c) or (b == d) or (abs(a - c) == abs(b - d))
    is_knight = (abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1)
    if is_queen:
        print("Угрожает ферзь")
    elif is_knight:
        print("Угрожает конь")
    else:
        print("никто не угрожает")


def hard_play_chess(a, b, c, d):
    next_steps = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                  (1, 2), (1, -2), (-1, 2), (-1, -2)
                  ]
    ret_value = "Конь вообще не угрожает :)"
    for step in next_steps:
        exp_c, exp_d = c + step[0], d + step[1]
        if (exp_c == a) and (exp_d == b):
            ret_value = "Конь угрожает уже сейчас, до хода"
            break

    for step in next_steps:
        next_a, next_b = a + step[0], b + step[1]
        if (next_a == c) and (next_b == d):
            ret_value = "Конь угрожает сразу же после хода"
            break
    print(ret_value)


print("Task 01:")
print(crazy_function_01(1.79))

print("\nTask 02:")
print(search_substr_02("First line", "This is the first line"))
print(search_substr_02("Second line", "This is the first line"))

print("\nTask 03:")
print(top_three_char("iueruwe wferfd cdfgf"))

print("\nTask 04:")
print(count_it("4234237468763456267345"))

print("\nTask 05:")
play_chess(1, 3, 5, 3)

print("\nTask 05 hard:")
hard_play_chess(1, 3, 5, 3)
hard_play_chess(3, 3, 5, 4)
