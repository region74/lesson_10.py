# Функция создает красивый резделитель из 10-и звездочек (**********)
def simple_separator():
    return '*' * 10


print(simple_separator() == '**********')  # True


# Функция создает разделитель из звездочек число которых можно регулировать параметром count
def long_separator(count):
    return '*' * count


print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


# Функция создает разделитель из любых символов любого количества
def separator(simbol, count):
    return simbol * count


print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    print('**********\nHello World!\n##########')
    return None


hello_world()


def hello_who(who='World'):
    print(f'**********\nHello {who}!\n##########')
    return None


hello_who()
hello_who('Max')
hello_who('Kate')


# Функция складывает любое количество цифр и возводит результат в степень power
def pow_many(power, *args):
    result = 0
    for i in args:
        result += i
    # return sum(args) ** power
    return result ** power


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


# Функция выводит переданные параметры в фиде key --> value, где key - имя параметра, value - значение параметра,:param kwargs: любое количество именованных параметров
def print_key_val(**kwargs):
    for name, age in kwargs.items():
        print(f'{name} --> {age}')
    return None


print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)


# Функция фильтрует последовательность iterable и возвращает новую Если function от элемента последовательности возвращает True,
# то элемент входит в новую последовательность иначе нет
def my_filter(iterable, function):
    # return list(filter(function,iterable))
    # или
    # result=[]
    # for item in iterable:
    #     if function(item):
    #         result.append(item)

    result = []
    for i in iterable:
        if function(i) == True:
            result.append(i)
    return result


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
