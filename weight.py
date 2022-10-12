print("This program converts lbs to kg and kg to lbs.")
weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ").lower()
if unit == 'l':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')
