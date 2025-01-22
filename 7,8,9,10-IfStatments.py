print("Welcom to simple calculator")
A = float(input("Enter a:"))
B = float(input("Enter b:"))

In = input("1 --> +\n2 --> -\n3 --> *\n4 --> /\n")

if In == "1":
    print(A+B)
elif In == "2":
    print(A-B)
elif In == "3":
    print(A*B)
elif In == "4":
    print(A/B)
else:
    print("Error")
