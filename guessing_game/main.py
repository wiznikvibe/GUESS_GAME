from random import randint
from art import logo
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5 

# Function for setting difficulty 
def set_difficulty():
    level = input("Choose Difficulty: 'easy', 'hard': \n")
    if level == 'easy':
        return EASY_LEVEL_TURN
    elif level == 'hard':
        return HARD_LEVEL_TURN

# Function for checking if the guess is right or wrong
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turn - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Function for Game
def game():
    print(logo)
    print("Welcome to guessing game!")
    
    
    guesses = set_difficulty()
    answer = randint(1, 100)
    guess = 0
    while guess != answer:
        guess = int(input("The number is between the range of 0-100, what is it?: \n"))
        print("I'm thinking of a number between 1 and 100.")
        
        print(f"Pssst, the correct answer is {answer}") 
        turns = check_answer(guess, answer, guesses)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()        


