principle = 0 
rate = 0 
time = 0 

while principle <= 0:
    principle = float(input("Enter principle:"))
    if principle <= 0 :
        print("Error")

while rate <= 0:
    rate = float(input("Enter rate:"))
    if rate <= 0 :
        print("Error")

while time <= 0:
    time = float(input("Enter time:"))
    if time <= 0 :
        print("Error")

all = principle * (1+rate/100)**time
print(all)
