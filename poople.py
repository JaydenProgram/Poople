import random
import sys

guess_word = ""
max_guesses = 0
guessed_words = []
formatted_guessed_words = {}

def prRed(s, noNewLine=False): print("\033[91m{}\033[00m".format(s), end="" if noNewLine else "\n")
def prGreen(s, noNewLine=False): print("\033[92m{}\033[00m".format(s), end="" if noNewLine else "\n")
def prYellow(s, noNewLine=False): print("\033[93m{}\033[00m".format(s), end="" if noNewLine else "\n")

def choose_random_word():
    words = []
    file_path = "words.txt"
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            words.append(line.rstrip().upper())
            line = file.readline()
            
    return random.choice(words)

def update_board(word):
    global guessed_words
    word_copy = []
    colors = []
    for j, char in enumerate(guess_word):
        word_copy.append(char)
        colors.append("\033[97m{}\033[00m")
    
    for j, char in enumerate(word):
        if char == guess_word[j]:
            colors[j] = f"\033[92m{char}\033[00m"
            word_copy.remove(char)
    for j, char in enumerate(word):
        if (char in word_copy and char != guess_word[j]):
            colors[j] = f"\033[93m{char}\033[00m"
            word_copy.remove(char)
    guessed_words.append({"word": word, "colors": colors})
    
def print_board():
    print()
    combined = []
    for entry in guessed_words:
        for i, char in enumerate(entry['word']):
            combined.append(f"{entry['colors'][i]}{char}")
            print(combined)
        print()
    for _ in range(max_guesses - len(guessed_words)):
        for _ in enumerate(guess_word):
            print(f"_", end="")
        print()
    print()

def init_game():
    global guess_word
    global max_guesses
    word = ""
    if len(sys.argv) > 1:
        word = sys.argv[1].upper()

    if word:
        guess_word = word
    else:
        guess_word = choose_random_word()
    max_guesses = len(guess_word) + 1
    
def start_game():
    while True:
        print_board()
        if len(guessed_words) >= max_guesses:
            prRed(f"Game over! Ran out of guesses: {len(guessed_words)} out of {max_guesses} guesses")
            break
        guess = input("Enter your guess: ").upper()
        if guess == "GIVE UP":
            print(guess_word)
            break

        if len(guess) > len(guess_word):
            prRed(f"Too much characters, you have: {len(guess)} characters, you need: {len(guess_word)} characters")
            continue
        elif len(guess) < len(guess_word):
            prRed(f"Too little characters, you have: {len(guess)} characters, you need: {len(guess_word)} characters")
            continue

        if guess != guess_word:
            update_board(guess)
        else:
            update_board(guess)
            prGreen("You won!")
            break



if __name__ == "__main__":
    init_game()
    start_game()