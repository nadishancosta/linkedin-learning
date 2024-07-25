secret_word = "giraffe"
usrGuess = input("Please enter your guess: ")
guessedright = False
tries=0
while not guessedright and tries<2:
    if usrGuess != secret_word:
        usrGuess = input(f"Incorrect, You have {2-tries} tries left.\nPlease re-enter the guess: ")
        tries += 1
    else:
        guessedright = True
        print("Correct guess dude! Amazing stuff!\nbye bye😂")

if tries >= 2:
    print("No more tries! Game over major looser!")