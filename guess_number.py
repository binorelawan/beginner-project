import random

def guess(x) :
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        try:
            guess = int(input('Guess number between 1 and {}: '.format(x)))
            if guess < random_number:
                print('Guess number to low')
            elif guess > random_number:
                print('Guess number to high')
        except:
            print('invalid input')
        
    
    print('CORRECT !!!!')

if __name__ == '__main__':
    guess(10)
    