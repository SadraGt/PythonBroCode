def show_balance(balance):
    print(f"your balance is : ${balance:.2f}")

def deposit():
    dep = float(input("Enter :"))
    if dep < 0:
        print("Error")
        return 0
    else:
        return dep

def withdraw(balance):
    wit = float(input("Enter :"))
    if wit > balance:
        print("Error")
        return 0
    else:
        return wit

def main():
    balance = 0
    run = True

    while run:
        print("1.Show Balance \n2.Deposit \n3.Withdraw \n4.Exit ")
        x = input("Enter your choice (1-4): ")

        match x:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                
                balance -= withdraw(balance)
            case "4":
                run = False
            case _:
                print("That is not a valid choive")

    print("have good day")

if __name__ == '__main__':
    main()