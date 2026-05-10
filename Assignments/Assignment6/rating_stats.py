"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    with open(filename, "r") as file:
        next(file)
        percent = {
            "M": [0, 0],
            "W": [0, 0],
        }
        for line in file:
            parts = line.split(",")
            percent[parts[1]][1] += 1 
            if float(parts[0]) > 3.5:
                percent[parts[1]][0] += 1
    M_percent = int((percent["M"][0] / percent["M"][1]) * 100)
    W_percent = int((percent["W"][0] / percent["W"][1]) * 100)
    print(f"{W_percent}% of reviews for women in the dataset are high.")
    print(f"{M_percent}% of reviews for men in the dataset are high.")
            
    # print(percent)


def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
