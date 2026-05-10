"""
File: betterphonebook.py
------------------
Program to show an example of using dictionaries to maintain
a phonebook.  This phonebook can store multiple phone numbers
for each person.
"""


def read_phone_numbers():
    """
    Ask the user for names, phone types, and numbers to story in a phonebook
    (dictionary of dictionaries).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phone_type = input("Type: ")
        if name not in phonebook:
            phonebook[name] = {}
        dict_for_person = phonebook[name]
        dict_for_person[phone_type] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/phone types/numbers in the phonebook.
    """
    for name in phonebook:
        print(name, "->", phonebook[name])


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name and phone type.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            dict_for_person = phonebook[name]
            phone_type = input("Type: ")
            if phone_type not in dict_for_person:
                print(name + " does not have a " + phone_type + " phone")
            else:
                print(dict_for_person[phone_type])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    print(phonebook)
    lookup_numbers(phonebook)


if __name__ == '__main__':
    main()
