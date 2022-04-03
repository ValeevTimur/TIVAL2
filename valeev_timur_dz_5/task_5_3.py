tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Николай', 'Тимур']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    while len(tutors) > len(klasses):
        klasses.append(None)
    d = dict(zip(tutors, klasses))
    i = 0
    for item in d.items():
        a = list(d.items())[i]
        i = i + 1
        yield a


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))

print(type(generator))