SENTINEL = 0    # the sentinel used to signal the end of the input

def main():
    values = []
    while True:
        val = int(input("Enter value: "))
        if val != SENTINEL:
            values = add_new_value(values, val)
        else:
            break
    print(f"The largest value is {values[0]}")
    print(f"The second largest is {values[1]}")


def add_new_value(values, value):
    l = len(values)
    if l < 1:
        values.append(value)
    elif l == 1:
        if values[0] >= value:
            values.append(value)
        else:
            values.insert(0, value)
    else:
        if values[0] <= value:
            values.insert(0, value)
        elif values[l-1] >= value:
            values.append(value)
        else:
            for i in range(0, l):
                if values[i] >= value and values[i+1] <= value:
                    values.insert(i+1, value)
    return values


if __name__ == '__main__':
    main()