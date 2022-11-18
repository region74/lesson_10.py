def print_house(height, wall_symbol='|'):
    for i in range(height):
        print(f'{wall_symbol}      {wall_symbol}')
    print('\n')


# Передача параметров по порядку
print_house(1, '#')
print_house(8, '$')
print_house(5)

# передача параметров по имени
print_house(wall_symbol='8', height=3)
print_house(height=2)
