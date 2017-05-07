### tceh python hw 2


## 1. Написать функцию, которая спрашивает пользователя число и степень числа,
#  возвращает число в степени.

def number_exp():
    ask_number = int(input("Please, enter a number: "))
    ask_exp = int(input("Please, enter an exponentiation: "))

    result = ask_number ** ask_exp
    return result

#print(number_exp())


## 2. Написать функцию для определения НОК для двух чисел.

def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

def noc(a, b):
    return a * b // nod(a, b)

# print(nod(8, 6))
# print(noc(8, 6))


## 3. Написать функцию, которая принимает список, и возвращает словарь
#  в формате: "тип данных: количество объектов"
#  count_types([1, 4, 'd']) -> {<class 'int'>: 2, <class 'str'>: 1}

def count_types(my_list):
    my_dict = {}

    for item in my_list:
        if type(item) not in my_dict:
            my_dict[type(item)] = 1
        else:
            my_dict[type(item)] += 1

    return my_dict

#print(count_types([1, 4, 'd']))


## 4. Написать функцию, которая принимает два словаря, сравнивает их ключи,
#  выдает в консоль сколько у них общих ключей

def compare_dicts(dict1, dict2):
    lst = []
    for key1 in dict1:
        for key2 in dict2:
            if key1 in key2:
                lst.append(key1)

    return len(lst)

dict1 = {'senya': 'almaz', 'sasha': 'ovsya', 'anya': 'ovsya', 'natasha': 'almaz'}
dict2 = {'misha': 'almaz', 'sasha': 'ovsya', 'anya': 'ovsya', 'irina': 'almaz'}

#print(compare_dicts(dict1, dict2))


## 5. Написать функцию, которая принимает любое количество аргументов,
#  она вернуть список типов, принятых аргументов
#  find_types(1, 's', []) -> [<class 'int'>, <class 'str'>, <class 'list'>]

def find_types(*args):
    hodor = []
    for arg_type in args:
        hodor.append(type(arg_type))
    return hodor

#print(find_types(1, 's', []))


## 6. Написать функцию, которая принимает на вход список списков (матрицу)
# и выводит ее в виде матрицы (один ряд на одной строке) в консоль

def list_of_lists(x):
    for matrix in x:
        print(matrix)

#list_of_lists([[3, 2, 1], ['a', 'b', 'c'], ['I', 'II', 'III']])


## 7. Написать функцию, которая принимает любое количество аргументов - списков,
#  она должна возвращать список из всех объектов списков, но каждый объект должен
#  быть уникальным join_lists([1, 2], ['a', 2], ['c', 1]) -> [1, 2, 'a', 'c']

def join_lists(*args):
    unique_list = []

    for arg in args:
        if arg not in unique_list:
            unique_list.extend(arg)

    return list(set(unique_list))

#print(join_lists([1, 2], ['a', 2], ['c', 1]))