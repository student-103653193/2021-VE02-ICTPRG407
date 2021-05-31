import random
attempt = 7
all = []
guesses = 0
n = random.randint(0,25)
print(n)
print("Hey there! Lets play a little guessing game""\nGuess the number between 0 and 25")
while attempt > 0:
    attempt -= 1
    guesses += 1
    guess = int(input("Enter Guess: "))
    if guess < n:
        print('Nope, its greater than that. \nYou have {} tries remaining.'.format(attempt))
        all.append(guess)
    elif guess > n:
        print('Nope, its less than that. \nYou have {} tries remaining.'.format(attempt))
        all.append(guess)
    else:
        break
if guess == n:
    print('Dam. You Win!' + '\nThe number was indeed:',guess,'\nYou guessed in',guesses, "guess.")
    print('Your guesses log: ')
    all.append(guess)
    print(all)
else:
    print('AHHAHA YOU LOOSE' + '\nThe number was:' ,n, 'you fool')
    print('Your guesses log: ')
    print(all)
