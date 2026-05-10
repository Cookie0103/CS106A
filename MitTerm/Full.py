import random

def main():
    rounds = 0
    consecutive = 0
    while consecutive < 2:
        rounds += 1
        toss1 = random.randint(0, 1)
        toss2 = random.randint(0, 1)
        print(f"Round # {rounds} - generated {toss1} and {toss2}")
        if toss1 == toss2:
            print("That's a success")
            consecutive += 1
        else:
            print("Sorry, that's not a success")
            consecutive = 0
    print(f"You simulated {rounds} rounds")
    


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()