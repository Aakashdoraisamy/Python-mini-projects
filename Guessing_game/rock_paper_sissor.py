import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissor']

while True:
    user_input = input('Type Rock/Paper/Scissor or Q to Quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Invalid input. Please choose Rock, Paper, or Scissor.")
        continue

    random_num = random.randint(0, 2)
    computer_pick = options[random_num]  # Referred by index value
    print('Computer Picked:', computer_pick)

    if user_input == computer_pick:
        print("It's a tie!")
        continue

    if user_input == 'rock' and computer_pick == 'scissor':
        print('You Won!')
        user_wins += 1

    elif user_input == 'scissor' and computer_pick == 'paper':
        print('You Won!')
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print('You Won!')
        user_wins += 1

    else:
        print('Computer Won!')
        computer_wins += 1

print('You won:', user_wins, 'times.')
print('Computer won:', computer_wins, 'times.')
print('Have a Nice Day!')
