list_1 = []
count = 1000
i = count
while i >= 1:
    list_1.append(i)
    i -= 1
list_1.reverse()
for i in list_1:
    if i % 2 == 0:
        list_1.remove(i)
print(list_1)
for number in range(1, 1000, 2):
    number = number ** 3
    if number % 7 == 0:
        print(number)


