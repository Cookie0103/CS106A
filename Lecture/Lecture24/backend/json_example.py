"""
File: json_example.py
---------------------
Provides an example of using json to read a file.
"""

import json


def main():
	file = open('ages.json')
	data = json.load(file)
	for name in data:
		age = data[name]
		print(name, age)

	# Create a string from the dictionary "data" and print it out
	str = json.dumps(data)
	print('String version of data: ' + str)


if __name__ == '__main__':
	main()
