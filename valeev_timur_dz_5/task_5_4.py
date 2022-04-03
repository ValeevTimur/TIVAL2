def get_numbers(src: list):
    figures_list = []
    n = max(src)
    for i in src:
        if i - n > 0:
            figures_list.append(i)
            n = i
        elif i - n < 0:
            n = i
    return figures_list

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))