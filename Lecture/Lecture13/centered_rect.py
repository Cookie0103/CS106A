"""
File: centered_rect.py
----------------------
This program draws several elements in a graphics canvas.
It also provides an example of how to center an object in
a canvas
"""

import tkinter

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 200     # Height of drawing canvas in pixels

def draw_centered_rect(canvas, width, height, rect_fill=None):
    """
    Draws a rectangle with the given width and height in the center of
    the canvas.  The rectangle can optionally be filled with a color
    given by the parameter rect_fill.
    """
    x = (CANVAS_WIDTH - width) / 2
    y = (CANVAS_HEIGHT - height) / 2
    canvas.create_rectangle(x, y, x + width, y + height, fill=rect_fill)


def drawing(canvas):
    """
    Draws two rectangles centered on the canvas.  One rectangle is a black
    outline.  The other is a filled blue rectangle.
    """
    draw_centered_rect(canvas, 200, 100)
    draw_centered_rect(canvas, 50, 25, rect_fill='blue')


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
