import random

lower_num, upper_num = 1, 10
max_attempts = 3
random_number = random.randint(lower_num, upper_num)
print(random_number)
print(f'Guess the number in the range from {lower_num} to {upper_num}.')


def get_guess():
    while True:
        try:
            guess_number = int(input("Guess: "))
            if guess_number > 10 or guess_number < 1:
                print("not within range, guess again")
            else:
                return guess_number
        except ValueError as e:
            print("invalid")


def check_guess(guess_number, random_number):
    if guess_number == random_number:
        return "You got it!"
    elif guess_number < random_number:
        return "The number is lower"
    elif guess_number > random_number:
        return "The number is higher"

def play_game():
    attempts = 0
    while attempts < max_attempts:
        attempts+=1
        guess = get_guess()
        result = check_guess(guess, random_number)
        if guess==result:
            print(f"you got itr! It's {random_number}")
            break
        else:
            print(f"{result}, guess again")
    else:
        print(f"you run out of times. The correct number is {random_number}")
play_game()