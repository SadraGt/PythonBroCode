# [start:end:stop]

X = "1234-5678-9012-3456"

# print(X[0])   #1
# print(X[:4])  #1234
# print(X[5:9]) #5678
# print(X[5:])  #5678-9012-3456
# print(X[-1])  #6
# print(X[::3])

# Delete site domain
SiteName = input("Enter sait name:")

A = (len(SiteName) - SiteName.rfind(".") ) * (-1 ) 
if SiteName.rfind(".") == -1:
    print("Error")
else:
    print(SiteName[:A])

