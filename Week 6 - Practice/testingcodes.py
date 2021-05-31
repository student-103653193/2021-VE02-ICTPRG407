import random
  
# Randomly choose winning number
winning_number = random.randint(1,10)
print("Debugging Aid: winning_number is '{}'".format(winning_number))  
  
# Limits user to four guesses
guesses_remaining = 4
  
print("You have four attempts to guess the correct number. Give it a shot!")
  
 
while  guesses_remaining > 0:
    guess = int(input("\nGuess a number between 1 and 10: "))
    guesses_remaining -= 1
    if guess == winning_number:
        print ("Winner! Winner! Chicken Dinner! You guessed the correct number. ")
        guesses_remaining = 0     # End game after correct guess.
    elif guesses_remaining == 0:
        print ("\nYou are out of tries! The winning number was:",winning_number, "\n\nBetter luck next time!")
    elif guesses_remaining == 1:
        print("\nSorry, that is not the correct number. Try again!  You have one try remaining.")
    else:
        print("\nSorry, that is not the correct number. Try again!  You have {} tries remaining.".format(guesses_remaining))