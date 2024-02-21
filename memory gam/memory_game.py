from list_of_words import words
import random
import time
import os

print(len(words))
list_of_words = []

# Get 10 Random words from the list of 2466 words
def generate_list():
    for i in range(10):
        word = random.choice(words)
        list_of_words.append(word)

    print('You will have 10 seconds to memorize these 10 words. You get 1 point for each word you can recall.\nThe 10 second countdown will start shortly.')
    for i in range(3, 0, 1):
        print(i, end='...\n',flush=True)
        time.sleep(1)

    time.sleep(3)
    print(list_of_words)
    for i in range(10, 0, -1):
        print(i, end="...\n", flush= True)
        time.sleep(1)
    print('\n' * 100)


def test_memory():
    lives = 3
    score = 0
    words_remaining = 10
    while lives > 0:
        try:
            user_word = input('What word do you remember? ').lower()
            if user_word in list_of_words:
                score += 1
                words_remaining -= 1
                print(f'Correct! Your score is now {score}.')
                print(f'There are {words_remaining} words remaining.')
            else:
                lives -= 1
                print(f'Wrong! You have {lives} guesses remaining.')
        except KeyboardInterrupt:
            print('You ended the game.')
        print(f'Current Score: {score}')
    print(f'Game Over. \nFinalScore: {score}')

def main():
    print('Welcome to the memory game. Pay close attention to the following list of words.')
    generate_list()
    test_memory()

main()