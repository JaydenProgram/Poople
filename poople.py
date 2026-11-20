import random
import sys

guess_word = ""
max_guesses = 0
guessed_words = []

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
    word_copy = []
    formatted_words_list = []
    for char in guess_word:
        word_copy.append(char)

    for char in word:
        formatted_words_list.append("\033[97m{}\033[00m".format(char))
    
    for j, char in enumerate(word):
        if char == guess_word[j]:
            formatted_words_list[j] = "\033[92m{}\033[00m".format(char)
            word_copy.remove(char)
    for j, char in enumerate(word):
        if (char in word_copy and char != guess_word[j]):
            formatted_words_list[j] = "\033[93m{}\033[00m".format(char)
            word_copy.remove(char)

    
    combined_word = "  ".join(formatted_words_list)
    guessed_words.append(combined_word)

def print_board():
    width = (len(guess_word) + len(guess_word) * 2)
    print("┏" + "━" * width + "┓")
    for entry in guessed_words:
        print("┃ " + entry + " ┃")
    underscore_list = []
    for _ in guess_word:
        underscore_list.append("_")
    underscore_string = "  ".join(underscore_list)
    for _ in range(max_guesses - len(guessed_words)):
        print("┃ " + underscore_string + " ┃")
    print("┗" + "━" * width + "┛")
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
            prRed(f"Game over! Ran out of guesses. The word was: {guess_word}")
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
            print_board()
            prGreen("You won!")
            break



if __name__ == "__main__":
    init_game()
    start_game()