import random

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
    if initialize:
        guess_word = word
    else:
        guessed_words.append(f"{word}")
        for word in guessed_words:
            for j, char in enumerate(word):
                if char == guess_word[j]:
                    prGreen(f"{char}")
                elif guess_word.find(char) != -1 and char != guess_word[j]:
                    prYellow(f"{char}")
                else:
                    print(f"{char}", end="")
            print()

def init_game():
    word = input("Enter word to guess for testing (Keep empty to randomize): ")
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
            print("You won!")
            break



if __name__ == "__main__":
    init_game()
    start_game()