import random 

Options = ("rock", "paper", "scissors")

while True:
    player = None
    computer = random.choice(Options)

    while player not in Options:
        player = input(f"enter a {Options}: ")

    if player == computer:
        print("tie!")
    elif player == "rock" and computer == "scissors":
        print("your win!")
    elif player == "paper" and computer == "rock":
        print("your win!")
    elif player == "scissors" and computer == "paper":
        print("your win!")
    else:
        print("your los!")

    Q = input("q for exit and enter for next game: ").lower()
    if Q == "q":
        break

    
