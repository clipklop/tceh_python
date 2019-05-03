#


# 1. Пользователь вводит число, если оно четное - выбрасываем 
#    исключение ValueError, если оно меньше 0 - TypeError, 
#    если оно больше 10 - IndexError. Обрабатываем ошибку,
#    говорим пользователю, в чем его ошибка
def errors(num):
    if num % 2 == 0:
        raise ValueError
    elif num < 0:
        raise TypeError
    elif num > 10:
        raise IndexError
    try:
        print(num)
    except:
        print('Yo! I caught an error!')


# 2. Создайте список произвольной длины. Пользователь должен ввести
#    индекс объекта, который хочет посмотреть. Если все
#    хорошо - пишите объект в консоль. Если нет - обработайте
#    возмозможные ошибки и скажите ему, что не так
def long_list(lst, i):
    try:
        return lst[i]
    except (ValueError, TypeError) as e:
        print(f'Kindly put a list as a first arg and index at the second {e}')
    except IndexError as e:
        print(f'Please, be more precise {e}')


# print(long_list([3, 3, 's', 'z', 'x', 'c', 4, 5, 6, 7, 8, 99], -1))
# print(long_list(2, 2))


# 3. Написать функцию, которая принимает на вход два аргумента. Если аргументы
#    больше нуля, возвращаем их сумму. Если оба меньше - разность.
#    Если знаки разные - возвращаем 0
def twoargs(x, y):
    return x + y if x > 0 and y > 0 else x - y if x < 0 and y < 0 else 0


# print(twoargs(-1, -53))


# 4. Написать функцию, которая принимает 3 аргумента - числа, найти среди них
#    два максимальных, вывести в консоль
def maxnum(*nums):
    x = []
    y = list(nums)
    while True:
        if len(y) == 1:
            return x
        x.append(y.pop(y.index(max(y))))


# print(maxnum(3, 9, 12))


# 5. Написать функцию, которая принимает два аргумента. Первый - список чисел,
#    второй - булевый флаг. Если флаг действителен - возвращаем новый список с
#    нечетными числами из входного списка, если флаг отрицателен - возвращаем
#    новый список с четными числами из входного списка
def boollist(lst, flag):
    return list(filter(lambda x: x % 2 == 0, lst)) if flag \
        else list(filter(lambda x: x % 2 != 0, lst))


# print(boollist([3, 2, 6, 7], False))


# 6. Написать функцию, которая принимает любое количество 
#    аргументов чисел. Среди них она находит максимальное
#    и минимальное. И возвращает оба
def anyargs(*nums):
    return min(nums), max(nums)


# print(anyargs(2, 3, 9, 15, 21))


# 7. Написать функцию, которая принимает два аргумента: строка
#    и булевый флаг case по-умолчанию равный True. Если флаг
#    действителен: возвращаем новую строку, где каждый символ входной
#    приведен к верхнему регистру, иначе - к нижнему
def caseflag(*string, case=True):
    return ''.join(string).upper() if case else ''.join(string).lower()

# print(caseflag('a', 'b', 'u', 'n', 'd', 'a', 'n', 't', case=False))


# 8. Написать функцию, которая принимает любое количество позиционных
#    аргументов - строк и один парматер по-умолчанию glue, который
#    равен ':'. Соединить все строки таким образом, чтобы в результат
#    попали все строки, длинее 3 символов. Для соединения между любых
#    двух строк вставлять glue
def glueargs(*args, glue=':'):
    return glue.join([arg for arg in args if len(arg) >= 3])


# print(glueargs('a', 'relu', 'ctant', 'rec', 'ede', 'b', 'c'))
