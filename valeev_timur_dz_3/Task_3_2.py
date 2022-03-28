def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    if value[0] == value[0].upper():
        value = value.lower()
        return dict_numbers[value].capitalize()
    else:
        return dict_numbers[value]


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

print(dict_numbers)
print('Выполнение задачи с учетом регистра:')
print(num_translate_adv("one"))
print(num_translate_adv("Two"))
print(num_translate_adv("tree"))
print(num_translate_adv("four"))
print(num_translate_adv("Five"))
print(num_translate_adv("six"))
print(num_translate_adv("seven"))
print(num_translate_adv("eight"))
print(num_translate_adv("Nine"))
print(num_translate_adv("ten"))

