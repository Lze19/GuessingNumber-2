import random as rd
import math

#=========================FUNCTIONS==============================

def valid_guess():
    while True:
        try:
            number = int(input("Your Guess: "))
            if number > 1000 or number < -1000:
               print("Guessed a Number BETWEEN -1000 and 1000")
            else:
                return number
        except ValueError:
            print("Input an Number Only Please!")

def play(scrt_number, user_guess):
        if user_guess > scrt_number:
            return "Too High"
        elif user_guess < scrt_number:
            return "Too Low"
        else:
            return "Correct!"

#=======================================MAIN=====================================
def main():
    secret_number = rd.randint(-1000,1000)
    print("Guess a number between -1000 and 1000")
    max_guess = math.log2(2001)
    count = 0
    while count < max_guess:
        guess = valid_guess()
        result = play(secret_number, guess)
        print(result)
        count += 1
        if result == "Correct!":
            print(f"You Guessed it in {count} times.")
            break
        else:
            print(f"Attemps Left: {max_guess-count:.0f}")
    else:
        print(f"You lost, You guessed {count} times.")
        print(f"The Secret Number is {secret_number}")

    again = input("Waht to Play Again (y/n):")
    if again != "y":
        print("Thanks for Playing")
    else:
        main()



main()