#Access to Marijuana
Country = input("Enter your Country:")
Age = int(input("Enter your Age:"))

if Country == "Canada" or Country == "canada":
    Country =  True
else:
    Country = False

if Country and Age >= 21:
    print("You have access.")
elif not Country or Age < 21 :
    print("You do not have access.")
elif Age <= 0 or Age >= 100:
    print("Age Error") 
else:
    print("Error")

