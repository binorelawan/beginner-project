import random


def password_generator():
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    
    length_password = int(input('How length is password you want ? '))
    count_password = int(input('How much password you want? '))

    for i in range(0, count_password):
        password = ''
        
        for j in range(0, length_password):
            char = random.choice(list(chars))
            password = password + char    

        print(f'Your password is: {password}')

if __name__ == '__main__':
    password_generator()