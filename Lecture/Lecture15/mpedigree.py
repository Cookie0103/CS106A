"""
File: mpedigree.py
------------------
Shows example of generating unique, hard-to-guess code numbers.
"""

import random


N_LABELS = 100
MAXNUM = 999999


def main():
	# prints a set of unique labels
	for i in range(N_LABELS):
		rand_value = random.randint(0, MAXNUM)
		rand_part = pad(rand_value, 6)
		unique_part = pad(i, 4)
		print(rand_part + unique_part)


# prepends 0s to string version of number
# until the str has length goal_length
def pad(number, goal_length):
	number_string = str(number)
	while len(number_string) < goal_length:
		number_string = '0' + number_string
	return number_string


if __name__ == '__main__':
	main()
