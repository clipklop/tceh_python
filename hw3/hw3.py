### tceh python hw 3
## Easy task.
#

# 1. Написать функцию, которая выбрасывает одно из трех исключений:
#    ValueError, TypeError или RuntimeError случайным образом.
#    В месте вызова функции обрабатывать все три исключения

def one_of_three(x):
    import random
    list_of_exceptions = random.choice([ValueError('ValueError'), TypeError('TypeError'), RuntimeError('RuntimeError')])

    try:
        x = 1 + x
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except RuntimeError:
        print("RuntimeError")
    finally:
        return list_of_exceptions

#print(one_of_three('s'))


# 2. Написать функцию, которая принимает на вход список, если
#    в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError

def list_func(my_list):
    sorted_int = []
    for i in my_list:
        if isinstance(i, int):
            sorted_int.append(i)
        else:
            raise ValueError()

    return sorted(sorted_int)

#print(list_func([4, 1, 6, 0, 9]))


# 3. Написать функцию, которая принимает словарь, преобразует все
#    ключи словаря к строкам и возвращает новый словарь

def take_dict(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        new_dict.update({str(key): value})

    return new_dict

#print(take_dict({1: 'one', 2: 'two', 3: 'three'}))


# 4. Написать функцию, которая принимает список чисел и возвращает их произведение

def number_list(x):
    # y = 1
    # for i in x:
    #     y *= i

    # return y
    from functools import reduce

    return reduce(lambda x, y: x * y, x)

#print(number_list([2, 4, 8, 16]))


# 5. Написать три функции: do_work, handle_success, handle_error.
#    do_work(my_list, success_callback, error_callback) принимает
#    на вход три аргумента: список, функцию для обработки успеха и функцию
#    для обработки ошибки. Ее задача проверить, что все значения в списке идут
#    по-возрастанию. Если все верно: вызываем success_callback, иначе: error_callback.
#    Функция handle_success пишет в консоль информацию об успешном выполнении.
#    Функция handle_error выбрасывает ValueError

def do_work(my_list, success_callback, error_callback):
    if my_list == sorted(my_list):
        handle_success()
    else:
        handle_error()

def handle_success():
    print("You've successfully called a function. Callback works!")

def handle_error():
    raise ValueError("Eww, error!")

print(do_work([2, 4, 8, 16], handle_success, handle_error))