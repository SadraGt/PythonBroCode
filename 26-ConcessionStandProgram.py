menu = {"pizza": 5.00,
        "nachos": 7.50,
        "fries": 9.99,
        "soda": 2.00
        }
tutal = 0
orde = []
for kay , value in menu.items():
    print(f"{kay:10}:{value:.2f}" )

while True:
    A = input("Enter aitem: ").lower()
    if A == "q":
        break
    elif menu.get(A) != None:
        orde.append(A)
        tutal += menu.get(A)

print(orde,end=" ")
print(tutal)


