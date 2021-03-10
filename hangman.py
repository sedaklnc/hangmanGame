import random
import sys


def display_hangman(guess):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[guess]


def open_file(name: str) -> list:
    try:
        with open(name, "r") as f:
            return list(filter(lambda x: len(x) > 3, f.read().split("\n")))
    except FileNotFoundError as err:
        print("I couldn't find the folder")
        sys.exit()


def change(pred: str, unk: list, word: str) -> list:
    for i in range(len(word)):
        if pred_word == word[i]:
            unk[i] = pred_word
    return unk


if len(sys.argv) != 2:
    print("misuse \npython hangman.py folder-name")
    quit()


file_name = sys.argv[1]
word = random.choice(open_file(file_name))


unk = ["_"] * len(word)
guess = 6
used = []
wrong_pred = []

print("LETS PLAY HANGMAN")

print("word length is: ", len(word))
print(display_hangman(guess))

while guess > 0:

    pred_word = input("enter a letter: ").lower()
    if pred_word in used:
        print("you already used")
        continue

    used.append(pred_word)

    if len(pred_word) > 1:
        print("Please enter a character (1)  ")
        continue

    if pred_word.isdigit():
        print("ups! enter a letter not digit")
        continue

    if pred_word in word:
        unk = change(pred_word, unk, word)
        print(" ".join(unk))

    else:
        guess -= 1
        print(f"wrong letter remainng chance: {guess} ")
        print(display_hangman(guess))
        wrong_pred.append(pred_word)

    if "_" not in unk:
        print("YOU WIN")
        quit()

    if guess == 0:
        print(f"word: {word}")


print(f"wrong predictions are {', '.join(wrong_pred)}")
