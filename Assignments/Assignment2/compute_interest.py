"""
File: compute_interest.py
-------------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    init_balance = float(input("Initial balance: "))
    start_year = int(input("Start year: "))
    start_month = int(input("Start month: "))
    end_year = int(input("End year: "))
    end_month = int(input("End month: "))
    if start_year > end_year:
        print("Starting date needs to be before the ending date.")
    elif start_year == end_year and start_month >= end_month:
        print("Starting date needs to be before the ending date.")
    else:
        interest_rate = float(input("Interest rate (0 to quit): "))
        while interest_rate != 0:
            earned = init_balance
            s_year = start_year
            s_month = start_month
            while (s_year<end_year) or (s_month<=end_month and s_year==end_year):
                print("Year ", s_year, "month ", s_month, "balance: ", earned)
                earned =  earned * (interest_rate + 1)
                s_month += 1
                if s_month == 13:
                    s_year += 1
                    s_month = 1
            interest_rate = float(input("Interest rate (0 to quit): "))
            s_year = start_year
            s_month = start_month
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
