SENTINEL = 0    # the sentinel used to signal the end of the input

def main():
    # 设置一个largest, second_largest就两个就找就行了
    print('This program finds the two largest integers entered by')
    print('the user.  Enter values, one per line, using a ' + str(SENTINEL))
    print('to signal the end of the input.')
    largest = -1
    second_largest = -1
    while True:
        value = int(input("Enter value: "))
        # 注意这个地方两个if是做不同的性质判断的话一定要分开来
        if value == SENTINEL:
            break
        if value > largest:
            second_largest = largest
            largest = value
        elif value > second_largest:
            second_largest = value
    
    
    print('The largest value is ' + str(largest))
    print('The second largest is ' + str(second_largest))
    
if __name__ == '__main__':
    main()