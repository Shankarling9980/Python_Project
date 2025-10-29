import random

# List of words to guess from
words = ["apple", "banana", "mango", "grape", "orange"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
chances = 6

print("Welcome to Hangman Game!")
print("_ " * len(word))

while chances > 0:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        chances -= 1
        print(f"Chances left: {chances}")

    # Show current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Check if word is guessed
    if "_" not in display_word:
        print("\n🎉 You won! The word was:", word)
        break

if chances == 0:
    print("\n😞 You lost! The word was:", word)