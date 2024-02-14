"""
Напишите функцию для разделения строки и преобразования ее в список
слов. Пример "Robin Singh" ==> ["Robin", "Singh"]
"""


def split_string(input_str) -> list:
    return input_str.split(" ")


print(split_string("Robin Singh" ))
