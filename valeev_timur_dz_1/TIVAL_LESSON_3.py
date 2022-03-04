def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    percent = ['процент', 'процента', 'процентов']
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2
    return str(n) + ' ' + percent[p]


for n in range(1, 101):
    print(transform_string(n))