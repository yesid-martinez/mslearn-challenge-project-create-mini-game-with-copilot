import random

def user_input():
    user_choice = input("Enter rock, paper, or scissors: ");
    choices = ["rock", "paper", "scissors"];
    while user_choice.lower() not in choices:
        print("Invalid input!");
        user_choice = input("Enter rock, paper, or scissors: ");
    return user_choice.lower();


def computer_choice():
    choices = ["rock", "paper", "scissors"];
    return random.choice(choices);

def compare(user, computer):
    if user == computer:
        return "It's a tie!";
    elif user == "rock":
        if computer == "scissors":
            return "You win!";
        else:
            return "You lose!";
    elif user == "scissors":
        if computer == "paper":
            return "You win!";
        else:
            return "You lose!";
    elif user == "paper":
        if computer == "rock":
            return "You win!";
        else:
            return "You lose!";
    else:
        return "Invalid input!";

def count_wins():
    user_wins = 0;
    computer_wins = 0;
    ties = 0;
    for i in range(5):
        user = user_input();
        computer = computer_choice();
        print(f"User: {user}");
        print(f"Computer: {computer}");
        result = compare(user, computer);
        print(result);
        if result == "You win!":
            user_wins += 1;
        elif result == "You lose!":
            computer_wins += 1;
        else:
            ties += 1;
    print(f"User wins: {user_wins}");
    print(f"Computer wins: {computer_wins}");
    print(f"Ties: {ties}");

def continue_playing():
    while True:
        answer = input("Do you want to continue playing? (yes/no): ")
        if answer.lower() == "yes":
            main()
            break
        elif answer.lower() == "no":
            print("Game Over!")
            break
        else:
            print("Invalid input!")

def main():
    while True:
        user = user_input()
        computer = computer_choice()
        print(f"User: {user}")
        print(f"Computer: {computer}")
        print(compare(user, computer))
        count_wins()

        while True:
            answer = input("Do you want to continue playing? (yes/no): ")
            if answer.lower() == "no":
                print("Game Over!")
                break
            elif answer.lower() == "yes":
                break
            else:
                print("Invalid input!")
        
        if answer.lower() == "no":
            break
main()