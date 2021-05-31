import random

rand = random.randint(0,1)
left = 7
log = []
guesses = 0
print(rand)
print("Hey there! Lets play a littel guessing gamer \nGuess the number between 0 to 25")
while left > 0:
    left -= 1
    guesses += 1
    guess = int(input("Enter Guess: "))
    log.append(guess)
    if (guess == rand):
        print("Damn. You win!\nThe number was indded",rand,"\nYou guessed in",guesses,"gusses")
        break
    elif (guess < rand):
        print("Nope, it's greater than that")
    elif (guess > rand):
        print("Nope, it's less than that")
    print("You have",left,"gusses left!")
else:
    print("AHAHAHA YOU LOOSE!")
    print("The number was",rand,"you fool")
print(log)