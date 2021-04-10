import random

random_number = random.randint(1,10)

player_guess = input("Guess the random number! (1-10): ")
player_guess = int(player_guess)

while True:
    if player_guess < random_number:
        print("Too low!")
        player_guess = input("Guess the random number! (1-10): ")
        player_guess = int(player_guess)
    elif player_guess > random_number:
        print("Too high!")
        player_guess = input("Guess the random number! (1-10): ")
        player_guess = int(player_guess)
    elif player_guess == random_number:
        print("You won!")
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again == "Y":
            random_number = random.randint(1, 10)
            player_guess = input("Guess the random number! (1-10): ")
            player_guess = int(player_guess)
        else:
            print("Thank you for playing!")
            break
    else:
        print("Please enter a valid input.")
        player_guess = input("Guess the random number! (1-10): ")
        player_guess = int(player_guess)
