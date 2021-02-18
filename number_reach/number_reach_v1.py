"""
Number Reach
Version 1

This is a text-based game.
Players compete with their own formula
to make up the goal number.
"""
import random

# Define Constants
INIT_NUMBER_POOL = {0}
INIT_NUMBERS = (1, 9)
INIT_COUNT = 2
GOAL_RANGE = (100, 999)
MAX_ANSWER = GOAL_RANGE[1] * 2
VALID_OPERATORS = ['+', '-', '*', '/']

# Ask how many players in the beginning
# and intiate a list of scores
def input_player_count_initiate_scores():
    player_count = 0
    while player_count <= 0:
        try:
            player_count = int(input('How many players play this game? '))
        except:
            print('Player Count must be an integer!')
    return [0 for idx in range(player_count)]

# Function: Initiate the number pool 
# with 0 and other two single digit numbers
def initiate_number_pool():
    num_pool = INIT_NUMBER_POOL.copy()
    for counter in range(INIT_COUNT):
        tmp_num = next(iter(num_pool))
        while tmp_num in num_pool:
            tmp_num = random.randint(INIT_NUMBERS[0], INIT_NUMBERS[1])
        num_pool.add(tmp_num)
    return num_pool

# Calculate the formula with first_num opr second_num
def calculate(first_num, opr, second_num):
    if opr == '+':
        return first_num + second_num
    elif opr == '-':
        return first_num - second_num
    elif opr == '*':
        return first_num * second_num
    elif opr == '/':
        return first_num // second_num
    else:
        return -1 * MAX_ANSWER   # Invalid Number

# Ask a player about his formula
# Validate the formula
# Check the answer of the formula
# return a tuple of (First_Number, Operator, Second_Number, Answer)
def ask_player_formula(player_idx, num_pool, num_goal):
    is_valid_formula = False
    while not is_valid_formula:
        print('== Hello Player ' + str(player_idx + 1) + ' ==')
        print('The goal is ' + str(num_goal))
        print('We got a pool of ' + str(num_pool))
        print('Please make up a formula.')
        # Ask the first number
        first_num = -1
        while first_num < 0 or first_num not in num_pool:
            try:
                first_num = int(input('First Number is: '))
            except:
                print('Your input is NOT a number! Please try again.')
            if first_num not in num_pool:
                print('Your input does NOT exist in the pool. Please try again.')
        # Ask the operator
        opr = ''
        while opr not in VALID_OPERATORS:
            opr = input('Operator: ')
            if opr not in VALID_OPERATORS:
                print('Please select a valid operator: ' + str(VALID_OPERATORS))
        # Ask the second number
        second_num = -1
        while second_num < 0 or second_num not in num_pool:
            try:
                second_num = int(input('Second Number is: '))
            except:
                print('Your input is NOT a number! Please try again.')
            if second_num not in num_pool:
                print('Your input does NOT exist in the pool. Please try again.')
        answer = calculate(first_num, opr, second_num)
        if answer < 0:
            print('The answer is INVALID. Please try again!')
        elif answer > MAX_ANSWER:
            print('The answer is too BIG. Please try again!')
        else:
            # Valid formula and answer
            is_valid_formula = True
            return (first_num, opr, second_num, answer)

# Initiate Overall Variables
is_playing = True
player_index = 0
player_scores = input_player_count_initiate_scores()

while is_playing:
    # 1. Initiate variables
    number_goal = random.randint(GOAL_RANGE[0], GOAL_RANGE[1])
    number_pool = initiate_number_pool()
    last_answer = -1

    while last_answer != number_goal:
        # 2. Ask a player about his formula
        # 3. Validate the formula
        # 4. Check the answer of the formula
        formula_tuple = ask_player_formula(player_index, number_pool, number_goal)

        # 5. Check the answer with the goal
        last_answer = formula_tuple[3]
        if last_answer == number_goal:
            # Win Message
            print('Congratulation! Player ' + str(player_index + 1) + ' wins.')
            print('{first_n} {opr} {second_n} = {ans}'.format(
                first_n = formula_tuple[0]
                , opr = formula_tuple[1]
                , second_n = formula_tuple[2]
                , ans = last_answer
            ))
            # Add 1 score to the player
            player_scores[player_index] += 1
            print('Player ' + str(player_index + 1) + ' got ' + str(player_scores[player_index]))
        else:
            # If not matched, add the answer to the pool
            number_pool.add(last_answer)
            # 5. Repeat with another player
            print('Next turn...')
            player_index = (player_index + 1) % len(player_scores)
    
    # 6. Show Score Result
    # and Ask players if they want to play again
    print('== Score Result ==')
    for plyr_idex, plyr_score in enumerate(player_scores):
        print('Player ' + str(plyr_idex + 1) + ': ' + str(plyr_score))

    play_again_reply = input('Do you want to play again? (Y/N) ')
    if play_again_reply.upper() != 'Y':
        is_playing = False

# End of the program
print('Goodbye :D')