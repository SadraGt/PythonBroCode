x = ''
while x == '':
    x = input(f"Enter your age:")
    if 0 < x < 200:
        x = ''

print(f"your age is : {x}")