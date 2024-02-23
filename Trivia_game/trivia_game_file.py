from questions_answers import trivia_questions_and_answers
import random

def main():
    while True:
        try:
            difficulty = input('Choose Difficulty. Enter "Easy", "Medium", or "Hard" to begin.')
            if difficulty.lower().strip() == 'easy':
                lives = 10
                break
            elif difficulty.lower().strip() == 'medium':
                lives = 6
                break
            elif difficulty.lower().strip() == 'hard':
                lives = 3
                break
        except ValueError:
            print('Please enter "Easy", "Medium" or "Hard".')
        except TypeError:
            print('Please enter "Easy", "Medium" or "Hard".')
    score = 0

    print(f'We are now beginning the trivia game. You will have {lives} attempts to answer as many questions correctly '
          f'as possible.')

    get_question_and_answers(score, lives)

def number_of_questions(max_questions):
    while True:
        try:
            num = int(input(f'How many questions would you like to be asked? (10-{max_questions}):' ))
            if 10 <= num <= max_questions:
                return num
            else:
                print(f'Please enter a number between 10 and {max_questions}.')
        except ValueError:
            print('Not a valid number. Try again.')

def get_question_and_answers(score, lives):

    # Randomize the order of questions
    random.shuffle(trivia_questions_and_answers)

    # Get the number of questions the user wants to be asked
    max_questions = len(trivia_questions_and_answers)
    num_questions = number_of_questions(max_questions)

    # slice the randomize list to get the desired number of questions
    selected_questions = trivia_questions_and_answers[:num_questions]

    #Print the Question to User
    for question in selected_questions:
        print(question['question'])
        correct_answer_key = question['answer']
        correct_answer_text = question[correct_answer_key]

        #Print the options to user
        for option in ['A', 'B', 'C', 'D']:
            print(f'{option}: {question[option]}')

        # Get user answer
        user_answer = input('Choose A, B, C, or D: ').upper().strip()
        while user_answer not in ['A', 'B', 'C', 'D']:
            print('Invalid option. Please type A, B, C, or D.')
            user_answer = input('Choose A, B, C, or D: ').upper().strip()

        # Check the answer
        if user_answer == question['answer']:
            score += 1
            print('Correct!')
        else:
            lives -= 1
            print(f'Incorrect. You have {lives} lives remaining.')
            print(f'The correct answer was {question["answer"]}: {correct_answer_text}')

    print(f'Your final score is {score}/{len(selected_questions)}', str(score/len(selected_questions) * 100) + '%.')

main()