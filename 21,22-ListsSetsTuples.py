#in note book

foods = []
prices = []
total = 0 

while True:
    food = input("Enter a food : ")
    if food == "q" or food == "Q":
        break
    else:
        price = float(input("Enter price : "))
    
        foods.append(food)
        prices.append(price)

i = 0
for food in foods:
    print(food, end=" ")
    print(prices[i])
    total += prices[i]
    i+=1
print(f"${total}")
