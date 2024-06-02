import random

# List of possible words
words = ["javascript", "hangman", "coding", "programming", "html", "css"]

def select_random_word():
    """Selects a random word from the list of words."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Returns the word display with guessed letters and underscores for unguessed letters."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    """Main function to play the Hangman game."""
    selected_word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(selected_word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses} / {max_incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            print("Correct!")
            if all(letter in guessed_letters for letter in selected_word):
                print("\nCongratulations! You guessed the word:", selected_word)
                break
        else:
            incorrect_guesses += 1
            print("Incorrect!")

        if incorrect_guesses == max_incorrect_guesses:
            print("\nGame Over! The word was:", selected_word)

if __name__ == "__main__":
    hangman()
