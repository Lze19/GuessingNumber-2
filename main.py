import random as rd

#=========================FUNCTIONS==============================

def valid_guess(number):
    while True:
        try:
           a = int(input("Your Guess: "))
           return a
        except ValueError:
            print("Input an Integer Only Please!")

def play(scrt_number, user_guess):
    count = 0
    while True:
        if user_guess > scrt_number:
            count += 1
            return "Too High"
        elif user_guess < scrt_number:
            count += 1
            return "Too Low"
        else:
            return f"Correct! You guessed it in {count} tries."

#=======================================MAIN=====================================

secret_number = rd.randint(-1000,1000)
print("Guess a number between -1000 and 1000")
guess = valid_guess()
