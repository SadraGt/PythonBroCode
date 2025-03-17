# def taxs(price, discount= 0, tax = 0.05):
#     print("price * (1-discount) * (1+tax)")
#     return price * (1-discount) * (1+tax)

# print(taxs(1000,0.1))

# import time

# def timers(end,start=1):
#     for x in range(start,end):
#         print(x)
#         time.sleep(1)

# timers(10)

# def hello(title,first,last,end=" "):
#     print(f"{title}{first}{end}{last}{end}")

# hello("Mr.","Sadra","gt",)

# def get_phone(cont, area, first, last):
#     print(f"{cont}-{area}-{first}-{last}")

# get_phone(1,123,456,7890)

# def jojo(*nums):
#     for num in nums :
#         print(f"{num} jojo")

# jojo(1,2,3,4,5)


# def test(**di):
#     for kay , value in di.items():
#         print(f"{kay}:{value}")

# test(name="sadra",age=20)


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")
    


shipping_label("Dr.", "Spongebob", "Squarepants",
               street= "123 fake St.",
               pobox="Po box #1001",
               city="Detroit",
               state="MI",
               zip="54321")
