
from random import randint
from typing import Any, Union

min = 1
roll_again = 'y'
while roll_again is 'y':

    max_num: str = input('How many sides should be on the dice?')

    max = int(max_num)

    dice = int(input('How many dice should we roll?'))
    print('''OK then, rolling...
    ...and your numbers are:''')

    for number in range(0, dice):
        assert isinstance(Union, object)
    number_current: Union[int, Any] = randint(min, max)

    print(number_current)
    roll_again = input('Would you like to roll again?')
