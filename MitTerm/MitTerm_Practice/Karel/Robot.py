from karel.stanfordkarel import *

# def return_to_start():
#     turn_around()
#     while front_is_clear():
#         move()
#     turn_around()

# def check_square_width():
#     length = 1
#     while front_is_clear():
#         move()
#         length += 1
#     return_to_start()
#     return length

# def main():
#     length = check_square_width()
#     if length == 3:
#         move()
#         turn_left()
#         move()
#         put_beeper()
#     else:
#         inner_length = length - 2
#         move_to_start()
#         put_inner_walls(inner_length-1)

# def move_to_start():
#     turn_left()
#     move()
#     turn_right()
#     move()

# def put_inner_walls(inner_length):
#     put_line(inner_length)
#     turn_left()
#     put_line(inner_length)
#     turn_left()
#     put_line(inner_length)
#     turn_left()
#     put_line(inner_length)


# def put_line(length):
#     for i in range(length):
#         put_beeper()
#         move()

# def turn_right():
#     for i in range(3):
#         turn_left()


# def turn_around():
#     turn_left()
#     turn_left()


if __name__ == "__main__":
    run_karel_program()