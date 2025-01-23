# x if condition y 

UserRole = "Admin"

AccessLevel = "Full Access" if UserRole == "Admin" or UserRole == "admin" else "Limited Access"

print(AccessLevel)
