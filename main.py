import random

flag = True
while True:
while flag:
    num = input('Type a number for an upper bound: ')

    if num.isdigit():
print('Let\'s play!')
num = int(num)
flag = False
else:
    print('Invalid input! Try again!')


secrect = random.randint(1, num)

guess = None
count = 1

while guess != secrect:
    guess = input('Please type in a number between 1 and ' + str(num) + ': ')
    if guess.isdigit():
        guess = int(guess)

        if guess == secrect:
            print('You\'ve got this')
            else print('please try again!')
            count += 1

print('it took you ' + count + 'guesses!')
