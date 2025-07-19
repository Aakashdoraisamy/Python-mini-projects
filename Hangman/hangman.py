import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)
print("The solution is :{}".format(chosen_word))

display = []
for _ in range(word_length):
    display += '_'
print(display)

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    
    if guess in display:
        print('You Already Guessed {}'.format(guess))

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print('You Guessed {} this particular Letter you Lose a Life'.format(guess))
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Lose...')
            break  

    print(f"{' '.join(display)}")
    
    if '_' not in display:
        end_of_game = True
        print('You Win...')

    if lives > 0: 
        print(stages[lives])
