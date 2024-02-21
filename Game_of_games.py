import random

# We are going to make a game of games... with 5 games and you will be successful.. when u lose, tell them their score
def main():
    score = 0
    play = start_game()
    if play:
        score = game_one(score)
        score = game_two(score)
        score = game_three(score)
        score = game_four(score)
        score = game_five(score)
    print(f'Your final score is {score}')


def start_game():
    while True:
        play = input('Do you want to play? (y/n): ').strip().lower()
        if play == 'y':
            print('Welcome to Game of Games.')
            return True
        elif play == 'n':
            print('Thank you. Goodbye.')
            return False
        else:
            print('please type y for yes or n for no')


# Game one will be the numbe guesser. You have 3 tries to guess a number 1-10.
def game_one(score):
    print('Welcome to the first game. This is the number guesser. You have 3 guesses to get the answer, which is 1-10.')
    answer = random.randint(1, 10)
    remaining_guesses = 3

    while remaining_guesses > 0:
        try:
            user_guess = int(input('Guess a number 1-10: '))
        except ValueError:
            print('That is not a valid integer. Please enter a number 1-10.')
            continue
        if answer == user_guess:
            print(f'Correct. You gain one point! ')
            score += 1
            break
        elif answer > user_guess:
            remaining_guesses -= 1
            if remaining_guesses != 0:
                print('Too Low! Try again. You have', remaining_guesses, 'guesses left.')
                continue
            else:
                print('You lose! The answer was', answer)
                break
            continue
        elif answer < user_guess:
            remaining_guesses -= 1
            if remaining_guesses != 0:
                print('Too high! Try again. You have', remaining_guesses, 'guess left.')
                continue
            else:
                print('You lose! The answer was', answer)
                break
            continue

    print(f'Your current score is {score}')
    return score

# Game Two: Rock Paper Scissors. Win One out of Three Games.
def game_two(score):
    print('Welcome to game 2, Rock Paper Scissors. Your current score is', score, 'You will have 5 attempts to beat the NPC. Each win is +1 in score.')
    options = ['rock', 'paper', 'scissors']

    chances_left = 5

    while chances_left > 0:
        user_choice = input('Type rock, paper, or scissors to start: ').lower().strip()
        if user_choice not in options:
            print('Please type rock, paper, or scissors.')
            continue
        bot_choice = random.choice(options)
        print('Bot picks', bot_choice + '.')

        if (user_choice == 'rock' and bot_choice == 'paper') or \
           (user_choice == 'paper' and bot_choice == 'rock') or \
           (user_choice == 'scissors' and bot_choice == 'paper'):
            score += 1
            print('You win! Current score:', score)
        else:
            print('You lose this round.\nCurrent Score:', str(score) +'.')
        chances_left -= 1
        print('You have', chances_left, 'games remaining.')
    return score

# Guess the word Game
def game_three(score):
    chances = 5
    print(f'You have {chances} chances to guess the word.')
    list_of_words = ['Banana', 'Capital', 'Longitude', 'Survey', 'Pokemon',' Apple', 'Syrup', 'Chocolate',
                     'Cereal', 'Blender', 'Python', 'Cheese', 'Cheddar', 'Crouton', 'Broccoli', 'Cauliflower',
                     'Cherry']
    random_word = random.choice(list_of_words)
    display_word = ['_' for _ in random_word]
    length_of_word = len(random_word)

    def get_hint(random_word):  # Mentioned the sun to the soil, directly—a sway to the lunar talk
        match random_word:
            case "Banana" | "Cherry" | "Apple":
                print("Hint: it's a fruit.")
            case "Capital" | "Longitude" | "Survey":
                print("Hint: it's related to geography or locations.")
            case "Pokemon" | "Python":
                print("Hint: it's related to different types of 'P' word entities - a game or a programming_language.")
            case "Syrup" | "Chocolate" | "Cereal" | "Cheese" | "Cheddar":
                print("Hint: it's something you might find in the kitchen.")
            case "Blender" | "Crouton" | "Broccoli" | "Cauliflower":
                print("Hint: it's something you might use in cooking or find in a dish.")
            case "Cauliflower" | "Broccoli":
                print("Hint: it's a vegetable.")
            case _:
                print("Hint: it's from a wide variety of answers, think broadly!")

    get_hint(random_word)

    while chances > 0:
        print(f"Word: {' '.join(display_word)}")
        print(f"Chances left: {chances}")
        user_guess = input('Guess a word: ').title().strip()
        if len(user_guess) != len(random_word):
            print(f'Please guess a word of the correct length ({length_of_word} characters).')
            continue
        matched = False
        for index, char in enumerate(random_word):
            if user_guess[index] == char:
                display_word[index] = char
                matched = True
        if matched and '_' in display_word:
            print('Nice. Some letters match.')
            chances -= 1
        elif '_' not in display_word:
            print(f'Congratulations. You guessed the word: {random_word}.')
            score += 1
            break
        else:
            print('No matching letters. Guess another word.')
            chances -= 1

    if chances <= 0:
        print(f"You've run out of chances. You lost at {display_word} and the word was {random_word}")

    print(f'Your current score is {score}')
    return score

# Game Four: Solve the math problems.
def game_four(score):
    print('Welcome to game 4. Solve the three problems to get up to three points. ')
    num1_choices = [5, 10, 15, 20, 7, 3, 4, 9, 13]
    operator_choices = ['*', '-', '+']
    num2_choices = [2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(3):
        problem_str = f'{random.choice(num1_choices)} {random.choice(operator_choices)} {random.choice(num2_choices)}'
        result = eval(problem_str)
        print(f'Problem #{i + 1}:')
        print(problem_str)

        try:
            answer = int(input('Answer: '))
            if answer == result:
                print('Good job, you did it. You gained 1 point.')
                score += 1
            else:
                print('Wrong. The answer was', str(result) + '.' + 'You answered', str(answer) + '.')
        except NameError:
            ...
        except ValueError:
            print('Please try again')
    print(f'Your current score is {score}')
    return score

# Game 5 -- Halving Game.. Choose a number. Half it correctly 5 times. Game stops when you get the answer wrong.
# Gain 1 point for each correct answer.
def game_five(score):
    beginning_num = int(input('Enter a Whole Number.'))
    game_five_score = 0

    for i in range(5):
        correct_answer = beginning_num / 2
        answer = float(input(f'What is {beginning_num} / 2?  '))

        if answer == correct_answer:
            score += 1
            game_five_score +=1
            print('Correct!')
        else:
            print(f'Wrong. You lose. You gained {game_five_score} total points from this game')
            return score

        beginning_num = correct_answer

    print(f'Well Done. You gained {game_five_score} total points from this game.')
    return score


main()