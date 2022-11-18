def multiplycation(*args):
    # print(type(args))
    # print(args)
    # print(len(args))
    result = 1
    for number in args:
        result *= number
    return result


print(multiplycation(2, 3))
print(multiplycation(2, 3, 4, 5))
print(multiplycation(2))


