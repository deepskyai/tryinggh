# Break the guess part of the guessing game into functions
# Make some tests that test the inputs of that game
# the tests should make sure the input is logical and correct

# Check to see if it is an int
# In the right range
# If it is in the right range, if you have selected a massive range have a warning that it will be an impossible game

from random import randint

answer = randint(1, 10)
print(answer)


def make_guess():
	try:
		guess = int(input(f'Guess a number between 1 and 10  '))
	except ValueError as err:
		print('Wrong input data type')

def run_guess(guess, answer):
	if 0 < guess < 11:
		if guess == answer:
			print('You\'re a genius!')
			return True
	else:
		print('I said 1 - 10')
		return False


# This is the game
if __name__ == '__main__':
	while True:
		try:
			guess = int(input('guess a number 1-10: '))
			if run_guess(guess, answer):
				break
		except ValueError:
			print('please enter a number')