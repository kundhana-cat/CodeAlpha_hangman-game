import random

words = ["python", "internship", "codealpha", "hangman"]
word = random.choice(words).upper()
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)
    
    guess = input("Guess a letter: ").upper()
    if guess in word:
        guessed_letters.append(guess)
    else:
        wrong_guesses += 1
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    
    if all(letter in guessed_letters for letter in word):
        print("You win!")
        break
else:
    print("You lose! Word was:", word)
