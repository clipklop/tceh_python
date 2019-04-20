# hw2


# Создать лист из 6 любых чисел. Отсортировать его по возрастанию
q = sorted(list(range(10, 0, -1)))
# print(q)


# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
w = {}
for i, item in enumerate(range(1, 6)):
    w[item] = str(i+1)
    # print(w)


# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
e = tuple(x / 10 for x in range(1, 11))
# print(max(e), min(e))


# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'
r = ' -> '.join(['Earth', 'Russia', 'Moscow'])
# print(r)


# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
t = '/bin:/usr/bin:/usr/local/bin'.split(':')
# print(t)


# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
y = ["Делятся на 7: " + str(i) if i % 7 == 0 else "Не делятся на 7: " + str(i) for i in range(1, 101)]
# print(y)


# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
# matrix = [[c for c in range(1, 4)] for r in range(4)]
# m = []
# for row in matrix:
#     m.append(row)
matrix = []
for row in range(0, 12, 3):
    matrix.append(list(range(0,12))[row:row+3])

for x in matrix:
    print(x[0], x[1], x[2])


# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
some_dicts = [
    {3: 'three',
    4: 'four',
    5: 'five'},
    {6: 'six',
    7: 'seven',
    8: 'eight'},
    {9: 'nine',
    10: 'ten',
    11: 'eleven'}
]
for i, item in enumerate(some_dicts):
    print(i, item)

# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
to_delete = ['keep-it', 'to-delete', 'keep-this', 'to-delete', 'please', 'to-delete']
no_to_delete = [i for i in to_delete if i != 'to-delete']
print(no_to_delete)


# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
u = list(range(10, 0, -1))
print(u)
