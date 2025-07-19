print('Welcome to Quiz! game....')

while True:
    user = input('DO You Want to Play?[yes/no]: ')
    if user.lower() != 'yes':
        break

    print('Ok lets Continue:-)')
    score = 0

    answer = input('What stands for CPU? ')
    if answer.lower() == 'central processing unit':
        print('Correct answer!')
        score += 1
    else:
        print('Better luck next time')

    answer = input('What stands for GPU? ')
    if answer.lower() == 'graphics processing unit':
        print('Correct answer!')
        score += 1
    else:
        print('Better luck next time')

    answer = input('What stands for RAM? ')
    if answer.lower() == 'random access memory':
        print('Correct answer!')
        score += 1
    else:
        print('Better luck next time')

    answer = input('What stands for ROM? ')
    if answer.lower() == 'read-only memory':
        print('Correct answer!')
        score += 1
    else:
        print('Better luck next time')

    answer = input('What stands for HTML? ')
    if answer.lower() == 'hypertext markup language':
        print('Correct answer!')
        score += 1
    else:
        print('Better luck next time')

    answer = input('What stands for CSS? ')
    if answer.lower() == 'cascading style sheets':
        print('Correct answer!')
        score += 1
    else:
        print('Better luck next time')

    print('Thanks for attending the Quiz....')
    print('Your Score at the End of the Quiz:',int(score/5*100),'%')


