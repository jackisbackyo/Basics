weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.lower() == 'l':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')