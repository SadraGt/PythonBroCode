import random

a = random.randint(1, 10)

while True:
    b = int(input("Enter a number 1-10 :"))
    if a == b :
        print(f"your win number is {a}")
        break
    
