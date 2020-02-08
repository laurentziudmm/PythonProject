#Conversion

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g or (T)ones or (C)ube : ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f'You are {converted} pounds')
elif unit.upper() == 'C':
    converted = weight + 0.45 + 143
    print(f'You are {converted} cube')
else:
    converted = weight + 0.45
    print(f'You are {converted} tones')



