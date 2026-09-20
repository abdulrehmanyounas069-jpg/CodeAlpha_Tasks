import random

word_list = ["Abdulrehman"]

max_attempts = 6


def play():
    word = random.choice(word_list)
    guessed = []
    wrong = 0

    print("Let's play Hangman!")
    print("The word has", len(word), "letters.")

    while wrong < max_attempts:
        display = ""
        for ch in word:
            if ch in guessed:
                display += ch + " "
            else:
                display += "_ "
        print("\n" + display)

        print("Wrong guesses:", wrong, "/", max_attempts)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already tried that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!")
        else:
            wrong += 1
            print("Wrong guess.")

        won = True
        for ch in word:
            if ch not in guessed:
                won = False
                break

        if won:
            print("\nYou guessed it! The word was:", word)
            return

    print("\nOut of tries! The word was:", word)


while True:
    play()
    choice = input("\nPlay again? (y/n): ").lower()
    if choice != "y":
        print("Thanks for playing!")
        break