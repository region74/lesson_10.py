# filter,sorted,map

friends = ['max', 'kate', 'ivan', 'leo']

result = []
for friend in friends:
    if friend.startswith('m'):
        result.append(friend)
print(result)


# тут типо написали как нужно фильтровать
def f(x):
    if x.startswith('m'):
        return True
    else:
        return False


# тут указываем по какой функции фильтровать и что фильтровать
result = filter(f, friends)

print(list(result))

# map

friends = ['max', 'kate', 'ivan', 'leo']

result = []
for friend in friends:
    result.append(friend.upper())
print(result)


def g(x):
    return x.upper()


# map
print(list(map(g, friends)))


# sorted()

def r(x):
    return x[-1]


print(sorted(friends, key=f))

# lambda_function

# f = lambda x: True if x.startswith('m') else False
# result = filter(f, friends)

# фильтр
result = filter(lambda x: True if x.startswith('m') else False, friends)

# мап
print(list(map(lambda x: x.upper(), friends)))

# сорт
print(list(sorted(friends, key=lambda x: x[-1])))
