from pprint import pprint
from collections import Counter


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    pass  # реализация
    # print(line)
    adr = line.split(' - - ')[0]
    return adr


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        # print(line)
        list_out.append(get_parse_attrs(line))
        """С помощью counter получаю словарь в формате ip:кол-во обращений к серверу и могу определить спамеров"""
        c = Counter(list_out)
        # list_out.sort()

pprint(c)
