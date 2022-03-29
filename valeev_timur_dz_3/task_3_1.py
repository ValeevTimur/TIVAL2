def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    str_out = dict_numbers.get(value)
    return str_out

dict_numbers = {
    "one": 'один',
    "two": 'два',
    "tree": 'три',
    "four": 'четыре',
    "five": 'пять',
    "six": 'шесть',
    "seven": 'семь',
    "eight": 'восемь',
    "nine": 'девять',
    "ten": 'десять'
}

for n in dict_numbers:
    print(num_translate(n))
print(num_translate("eleven"))