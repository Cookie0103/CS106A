"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill2.txt'


def main():
    """
    Add your code (remember to delete the "pass" below)
    """
    store_dict = {}
    with open(INPUT_FILE, "r") as file:
        for line in file:
            start = line.find("[")
            end = line.find("]")
            store = line[start+1: end]
            money = line[end+3: ]
            store_dict[store] = store_dict.get(store, 0) + int(money)
    # print(store_dict)
    for key, value in store_dict.items():
        print(key, ": $", value, sep="")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
