import random

choice = ['rock', 'paper', 'scissors']

def hompimpa(x):
    num = 0
    while num < x:
        computer = random.choice(choice)
        guess = input("choice 'rock', 'paper', 'scissors': ").lower()

        if guess not in choice:
            print('You choose wrong answer, please choose again.')
            num -= 1
        elif guess == computer:
            print('It\'s a tie ! You and Computer choose {}'.format(guess))
        elif (guess == 'rock' and computer == 'scissors') or (guess == 'scissors' and computer == 'paper') \
            or (guess == 'paper' and computer == 'rock'):
            print('You are the winner ! You choose {} and Computer choose {}'.format(guess, computer))
        else :
            print('You are the loser. You choose {} and Computer choose {}'.format(guess, computer))

        num += 1

if __name__ == '__main__':
    hompimpa(3)