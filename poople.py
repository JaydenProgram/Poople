import random
import sys

guess_word = ""
guessed_words = []

def prRed(s): print("\033[91m{}\033[00m".format(s), end="")
def prGreen(s): print("\033[92m{}\033[00m".format(s), end="")
def prYellow(s): print("\033[93m{}\033[00m".format(s), end="")

def choose_random_word():
    words = []
    file = open("words.txt", "r")
    line = file.readline()
    while line:
        words.append(line.rstrip())
        line = file.readline()

    file.close()

    words_len = len(words)
    return words[random.randint(0, words_len - 1)]

def update_board(initialize, word):
    global guess_word
    global guessed_words
    word_copy = []
    colors = []
    if initialize:
        guess_word = word
        print(guess_word)
    else:
        for j, char in enumerate(guess_word):
            word_copy.append(char)
            colors.append("grey")
        
        for j, char in enumerate(word):
            if char == guess_word[j]:
                colors[j] = "green"
                word_copy.remove(char)
        for j, char in enumerate(word):
            if (char in word_copy and char != guess_word[j]):
                colors[j] = "yellow"
                word_copy.remove(char)

        guessed_words.append({"word": word, "colors": colors})
        for word in guessed_words:
            for i, char in enumerate(word['word']):
                if word['colors'][i] == "green":
                    prGreen(f"{char}")
                if word['colors'][i] == "yellow":
                    prYellow(f"{char}")
                elif word['colors'][i] == "grey":
                    print(f"{char}", end="")
            print()

def init_game():
    word = ""
    if len(sys.argv) > 1:
        word = sys.argv[1]

    if word:
        update_board(True, word)
    else:
        update_board(True, choose_random_word())
    
def start_game():
    while True:
        guess = input("Enter your guess: ")
        if len(guess) != len(guess_word):
            print(f"Not enough characters, {len(guess), len(guess_word)}")
            continue

        if guess != guess_word:
            update_board(False, guess)
        elif guess == "Give Up":
            print(guess_word)
            break
        else:
            prGreen("You won!")
            print()
            break



if __name__ == "__main__":
    init_game()
    start_game()