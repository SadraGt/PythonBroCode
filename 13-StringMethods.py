Number = input("Enter your number:+98")

if Number.find("9") != 0:
    print("Error The number is wrong.")
elif len(Number) != 10:
    print("Error your number is not 13 number")
elif not Number.isdigit():
    print("Error use only number")
else:
    print(f"Welcome")


    

