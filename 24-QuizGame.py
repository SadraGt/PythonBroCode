sovals = ("1-bist car for offroad?",
          "2-in barnme chand soval darad?",
          "3-how i'm i?")
javabs = (     ("A.awd","B.4wd","C.fwd","D.rwd"),
               ("A.3","B.4","C.5","D.6"),
               ("A.ali","B.babak","C.sadra","D.janatan"))
javabdorost = ["B","A","C"]
shomariSoval = 0 
emtiaz = 0

for soval in sovals:
    print(soval)
    print(javabs[shomariSoval])
    javabuser=input("Enter: ").upper()
    if javabuser == javabdorost[shomariSoval]:
        emtiaz += 1
        print("dorost")
    else:
        print("nadorost")

    shomariSoval +=1

print(f"{emtiaz} az {len(sovals)}")

