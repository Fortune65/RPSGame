import random
user_score = 0
comp_score = 0

while True:
    user_action = input("Enter a choice [rock, paper, scissors]:")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"\nIts a tie! Both players have selected {user_action}.\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win and computer loses!")
            user_score = user_score + 1
            comp_score = comp_score - 1
        else:
            print("Paper covers rock! You lose and computer wins!")
            user_score = user_score - 1
            comp_score = comp_score + 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win and computer loses!")
            user_score = user_score + 1
            comp_score = comp_score - 1
        else:
            print("Scissors cuts paper! You lose and computer wins!")
            user_score = user_score - 1
            comp_score = comp_score + 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win and computer loses!")
            user_score = user_score + 1
            comp_score = comp_score - 1
        else:
            print("Rock smashes scissors! You lose and computer wins!")
            user_score = user_score - 1
            comp_score = comp_score + 1
    play_again = input("\nPlay again? (y/n): ")
    if play_again != "y":
        print(f"\nYour final score is {user_score} and the computer's final score is {comp_score}.")
        break
