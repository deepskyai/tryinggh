from random import randint
import sys

# This version has a bunch of comments from when I tried to figure out git
# Then I added THIS COOL COMMENT yeah
# The feature was now changed back

a = int(sys.argv[1])
b = int(sys.argv[2])

target = randint(a, b)
print(target)

while True: # This while loops lets you enter it and keeps it going without too much fuss
    try:
        guess = int(input(f'Guess a number between {a} and {b}  '))
        if a <= guess <= b:
            if guess == target:
                print('You are  a genius!')
                break
        else:
            print(f'I said {a} to {b}  ')
    except ValueError:
        print('Please print a number')
        continue