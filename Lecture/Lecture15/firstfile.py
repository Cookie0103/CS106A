"""
File: firstfile.py
------------------
Read all the lines in the file example.txt
and print them to the screen
"""


FILENAME = 'example.txt'

def main():
	# 1. open the file
	with open(FILENAME, 'r') as file:
		# 2. read the file one line at a time
		for line in file:
			# 3. get rid of newline at the end of the line
			line = line.strip()
			print(line)


if __name__ == '__main__':
	main()
