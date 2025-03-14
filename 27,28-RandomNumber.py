import random

low = int(input("Enter low number: "))
hi = int(input("Enter hi number: "))

num = random.randint(low, hi)

while True:
    g = int(input("Enter your g: "))

    if g < low or g > hi:
        print(f"Error {g} is out of range!")
    elif num == g :
        print(f"your win {num} is True ")
        break
    elif g < num:
        print("too low")
    elif g > num:
        print("to hi")