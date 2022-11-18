def print_house(wall_symbol='|'):
    for i in range(4):
        print(f'{wall_symbol}      {wall_symbol}')
    print('\n')


print_house('#')
print_house('$')
print_house()
