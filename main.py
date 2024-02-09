import random 

possible_choices = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors",
}

winning_combination = {
    "Rock":"Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

user_score = 0
computer_score = 0

def player_choice():
    choice = input(f"Enter your choice from the below possible choices\n {possible_choices} :\n")
    if choice in possible_choices:
        return possible_choices[choice]
    else:
        return player_choice()
    
def get_victor():
    computer_choice = possible_choices[str(random.randrange(1,4))]
    user_choice = player_choice()
    if winning_combination[user_choice] == computer_choice:
        global user_score
        user_score+=1
        print("\nUser Wins!\n")
    elif winning_combination[computer_choice] == user_choice:
        global computer_score
        computer_score+=1
        print("\nComputer Wins!\n")
    else:
        print("\nDraw!\n")

def continue_choice():
    choice = input("\nDo you want to continue\nEnter yes or y to continue or no or n to quit: ")
    if choice.lower() == "yes" or choice.lower() =="y":
        return True
    elif choice.lower() == "no" or choice.lower() == "n":
        return False
    else:
        return continue_choice()
    
def play_game():
    continue_playing = True
    while(continue_playing):
        get_victor()
        continue_playing = continue_choice()
    print("\nUser Score:",user_score)
    print("Computer Score:", computer_score)
    if user_score>computer_score:
        print("\nUser Wins!")
    elif computer_score>user_score:
        print("\nComputer Wins!")
    else:
        print("\nDraw")

def main():
    play_game()


if __name__ =="__main__":
    main()

        

