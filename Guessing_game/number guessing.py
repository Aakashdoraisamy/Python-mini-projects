import random

while True:  # Start the game loop
    top_of_range = int(input('Enter a digit: '))

    # Input validation
    if top_of_range <= 0 or top_of_range >= 10:

        print('Enter a number greater than zero  and enter less than 10 ')
        quit()  # Stop if the number is invalid
    else:
        print('Process will continue')

    # Generate a random number within the range
    random_number = random.randint(1, top_of_range)
    print("A random number has been chosen between 1 to 10 and your number.")

    # Allow user to guess the number
    attempts = 0
    while True:
        user_guess = int(input('Guess the random number: '))
        attempts += 1

        # Check if the guess is correct
        if user_guess == random_number:
            print(f'Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.')
            break
        elif user_guess < random_number:           
            print('Your guess is too low. Try again!')
        else:
            print('Your guess is too high. Try again!')

    # Option to play again
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        print('Thanks for playing! Goodbye.')
        break  # Exit the game loop if the user doesn't want to play again
