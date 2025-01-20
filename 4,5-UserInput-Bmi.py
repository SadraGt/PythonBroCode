name = input("your name?")
Tall = float(input("How tall are you? (cm)")) /100
Weigh = float(input("How much do you weigh?"))

Tall2 = Tall*Tall
Bmi = Weigh / Tall2

if bool(name):
    print(f"Hi {name} Your bmi is : {Bmi}")
else:
    print(f"Hi nobady")


