"""
File: firstrectangle.py
-----------------------
This program draws a rectangle in a graphics canvas.
"""

import tkinter

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 200     # Height of drawing canvas in pixels


def drawing(canvas):
    canvas.create_rectangle(20, 20, 100, 100)


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
