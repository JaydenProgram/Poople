import argparse
import random

def parse_words():
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", help="Leave empty to get random word")
    return parser.parse_args()

def choose_random_word():
    words = []
    file = open("words.txt", "r")
    line = file.readline()
    while line:
        words.append(line)
        line = file.readline()

    file.close()

    words_len = len(words)
    return words[random.randint(0, words_len - 1)]

def start_game(word):
    if word:
        print(word)
    else:
        print(choose_random_word())

if __name__ == "__main__":
    args = parse_words()
    start_game(args.word)