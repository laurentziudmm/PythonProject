def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prBlue(prt): print("\033[34m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))


color = input('What is your favorite color? : ')
flower = input('But what color do you like on flowers? ')
s = '#' * 45

if color.upper() == 'RED':
    converted = ('\033[91m Red \033[00m')
elif color.upper() == 'BLUE':
    converted = ('\033[34m Blue \033[00m')
elif color.upper() == 'YELLOW':
    converted = ('\033[93m Yellow \033[00m')
elif color.upper() == 'PURPLE':
    converted = ('\033[95m Purple \033[00m')
else:
    converted = ('\033[92m Green \033[00m')

if flower.upper() == 'RED':
    converted1 = ('\033[91m Red \033[00m')
elif flower.upper() == 'BLUE':
    converted1 = ('\033[34m Blue \033[00m')
elif flower.upper() == 'YELLOW':
    converted1 = ('\033[93m Yellow \033[00m')
elif flower.upper() == 'PURPLE':
    converted1 = ('\033[95m Purple \033[00m')
else:
    converted1 = ('\033[92m Green \033[00m')
    
print (f' {s} \n ' + '\n' + f' You like {converted1} color on flowers and, \n'    + f'{converted} color on your home color!! \n ')



# flower = input('But what color do you like on flowers? ')
# unit = input('Red or Blue or Yellow or Cyan: ')

# s = '#' * 45

# if color.upper() == 'Red':
#      prRed = f'{color}'
    
# elif color.upper() == 'Blue':
#     prBlue  = f'{color}'
# elif color.upper() == 'Yellow':
#     color = f'prYellow{color}'
# else :
#     color = f'prCyan{color}'

# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f'You are {converted} kilos')
# elif unit.upper() == 'K':
#     converted = weight / 0.45
#     print(f'You are {converted} pounds')


# print(f'{color}')


# print (f' {s} \n ' + '\n' + f' You like {flower} color on flowers and, \n'    + f'{color} color on your home color!! \n ')