import json

# I have used this word so I can test the program and ensure it works. It would be very easy to download a word list
# and then use the random library to randomly select one word from that list and use that instead of the static set word

word_to_be_guessed = "hangman"
letters_guessed = []
acceptable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

for i in word_to_be_guessed:
    letters_guessed.append("-")

with open("hangman_graphics.json") as f:
    data = json.load(f)

running = True
counter = 0
lives = 0

while running is True:
    print(f"\nDisplay: {''.join(letters_guessed)}\n")
    guess = input("Please enter your guess > ").lower()

    if len(guess) > 1:
        print("\nThat guess was longer than a single character and therefore has not been considered.")
    elif guess not in acceptable:
        print("\nSorry that was not a valid alphabetic character and therefore has not been considered.")
    else:
        if guess in word_to_be_guessed:
            print(f"\nThe letter {guess} was in the word!")
            for i in range(len(word_to_be_guessed)):
                if guess == word_to_be_guessed[i]:
                    letters_guessed[i] = guess
        else:
            lives += 1
            print(f"\nThe letter {guess} was not in the word...")
            print(f"\n{data['graphics'][lives]}")
            if lives == 6:
                running = False
                print(f"\nYou did not manage to guess the word and have now been hung...\n"
                      f"The word was \"{word_to_be_guessed}\"")

        counter += 1

        if (''.join(letters_guessed)) == word_to_be_guessed:
            running = False
            print(
                f"\nCongratulations you have successfully guessed the word "
                f"\"{word_to_be_guessed}\" in just {counter} attempts!")
