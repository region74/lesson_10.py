# передача функции в функцию

def print_who(name):
    print(name)


print_who('Max')

p = print_who('Max')
print_who(p)

p = print_who
print_who(p)
print(p)
print(type(p))

p('leo')

def other(name,func):
    # вызов переданной функции внутри другой функции
    func(name)
other('kolya',print_who)
other('ivan',p)


