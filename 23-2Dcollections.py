# # food = ["apple", "orange", "banana", "coconut"]
# # vegetables = ["celery", "carrots", "potatoes"]
# # meats = ["chicken", "fish", "turkey"]

# # groceries = [food, vegetables, meats]

# groceries = [   ["apple", "orange", "banana", "coconut"],
#                 ["celery", "carrots", "potatoes"],
#                 ["chicken", "fish", "turkey"]]


# #print(groceries)
# #print(groceries[0])        #عدد رو میدی و اون ارایه یک بعدی رو بهت میده 
# #print(groceries[0][0])     #اندیس هارو میدی و خروجی چاپ میکنه

# for collection in groceries:
#     #print(collection)
#     for food in collection:
#         print(food, end=" ")

NP = [[1,2,3],
      [4,5,6],
      [7,8,9],
      ["*",0,"#"]
      ]

for row in NP:
    for num in row:
        print(num, end=" ")
    print()