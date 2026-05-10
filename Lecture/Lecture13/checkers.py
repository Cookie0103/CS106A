"""
File: checkers.py
-----------------
This program displays a checkerboard on the graphics canvas
"""

import tkinter

CANVAS_WIDTH = 800      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels

ROWS = 20                # Number of rows in checkerboard
COLS = 6                # Number of columns in checkerboard


def get_color(row, col):
    """
    Determines the color of the checkerboard square (white or black)
    based on its location on the checkerboard.  Squares whose
    (row + column) is an even number are white, otherwise they are
    black.
    """
    if (row + col) % 2 == 0:
        return 'white'
    return 'black'


def draw_square(canvas, row, col):
    """
    Draws a single checkerboard square on the canvas at the given (row, col)
    in the checkboard.
    """
    sq_size = CANVAS_HEIGHT / ROWS
    x = col * sq_size
    y = row * sq_size
    color = get_color(row, col)
    canvas.create_rectangle(x, y, x + sq_size, y + sq_size, fill=color)


def drawing(canvas):
    """
    Draws a checkerboard pattern in the canvas, based on the constants specifying
    the number of ROWS and COLS in the checkerboard.
    """
    for row in range(ROWS):
        for col in range(COLS):
            draw_square(canvas, row, col)


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    drawing(canvas)
    tkinter.mainloop()


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('graphics')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


if __name__ == '__main__':
    main()
