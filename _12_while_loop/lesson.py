counter = 1
while counter <= 5:
    print(f'counter = {counter}')
    counter += 1

my_list  = [1, 33, 45, 3, 55]
while my_list:
    new_list = my_list.pop()
    print(my_list)


#

import random

HEADS = 'heads'
TAILS = 'tails'
COIN_VALUES = [HEADS,TAILS]
def flip_coin():
    return random.choice(COIN_VALUES)

print(flip_coin())
