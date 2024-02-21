import string

from words import adjectives_list, verbs_list, words, nouns_list
import random

def get_valid_word(words):
    word1 = random.choice(words)
    word2 = random.choice(words)
    while '-' in word1 or ' ' in word1:
        word1 = random.choice(words)
    while '-' in word2 or ' ' in word2:
        word1 = random.choice(words)
    combined_word = word1 + ' ' + word2
    return combined_word

def generate_phrase():
    word1 = random.choice(nouns_list)
    word2 = random.choice(adjectives_list)
    word3 = random.choice(verbs_list)

    while '-' in word1 or ' ' in word1:
        word1 = random.choice(nouns_list)
    while '-' in word2 or ' ' in word2:
        word2 = random.choice(adjectives_list)
    while '-' in word3 or ' ' in word3:
        word3 = random.choice(verbs_list)

    phrase = random.choice([(word2, word1), (word1, word3), (word2, word3)])

    phrase_pair = ' '.join(phrase)

    return phrase_pair

def hangman():
    answer = generate_phrase().upper()
    answer_letters = set(answer)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 10

    while len(answer_letters) > 0 and lives > 0:
        # letters used
        print('You have used these letters: ',''.join(used_letters))

        # what current word is ( ie w _ r d)
        word_list = [letter if letter in used_letters else ('  ' if letter == ' ' else '-') for letter in answer]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in answer_letters:
                answer_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f'Letter is not in this word. -1 life. {lives} lives remaining.')
        elif user_letter in used_letters:
            print('You have already guessed that character. Please try again')
        else:
            print('Invalid character. Please try again.')

    if lives > 0:
        print('You win. Congratulations!')
    else:
        print(f'You lose. The word was {answer}')
    #play again?
    play_again = input('Want to play again? y/n').lower().strip()
    if play_again == 'y':
        hangman()
    else:
        print('have a good day.')

hangman()