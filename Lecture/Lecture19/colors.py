"""
File: colors.py
---------------
This program allows the user the see examples of different
colors (as defined by their RGB values).  An initial set of
colors (and RGB values) is read from a file.  The user can
also specify custom RGB values to see the color produced.
"""

import tkinter


CANVAS_WIDTH = 600                      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300                     # Height of drawing canvas in pixels
RECTANGLE_WIDTH = 400                   # Width of color rectangle in pixels
RECTANGLE_HEIGHT = 200                  # Height of color rectangle in pixels
COLORFILE = 'data/ColorTuples.csv'      # File of color names and rgb values


def load_colors(filename):
    """
    Loads colors from a comma separated value file where each
    line defines a color based on RGB values, as follows:
    <color name>, <red>, <green>, <blue>
    Returns a dictionary with color names as keys and RGB tuples as values.
    """
    color_dict = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split(',')
            color_name = parts[0]
            r = int(parts[1])
            g = int(parts[2])
            b = int(parts[3])
            color_dict[color_name] = (r, g, b)
    return color_dict


def list_colors(colors):
    """
    Lists all the colors in the dictionary of colors -> RGB values passed in
    """
    print("List of all color names:")
    for color in colors:
        print(color)


def get_color_tuple():
    """
    Asks the user for  red, green, and blue values (for a color)
    and returns a tuple (red, green, blue) of the values entered.
    """
    red = int(input('Enter red: '))
    green = int(input('Enter green: '))
    blue = int(input('Enter blue: '))
    return red, green, blue


def draw_rectangle(canvas, rgb_tuple):
    """
    Draws a rectangle on the given canvas, where the color of the
    rectangle is determined by the tuple of RGB values passed in.
    """
    # Create hexadecimal string of RGB colors: #RRGGBB
    hex_red = "%02x" % rgb_tuple[0]
    hex_green = "%02x" % rgb_tuple[1]
    hex_blue = "%02x" % rgb_tuple[2]
    hex_color = "#" + hex_red + hex_green + hex_blue

    # Determine coordinates to center rectangle in canvas
    x = (CANVAS_WIDTH - RECTANGLE_WIDTH) // 2
    y = (CANVAS_HEIGHT - RECTANGLE_HEIGHT) // 2

    # Draw rectangle
    canvas.create_rectangle(x, y, x + RECTANGLE_WIDTH, y + RECTANGLE_HEIGHT,
                            fill=hex_color, outline=hex_color)


def make_canvas(width, height):
    """
    Creates and returns a drawing canvas  of the given width
    and height, ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('colors')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
    return canvas


def main():
    colors = load_colors(COLORFILE)
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    while True:
        name = input('Enter a color ("list" to see all color names): ')
        if name == '':
            break
        elif name == 'list':
            list_colors(colors)
        elif (name != 'custom') and (name not in colors.keys()):
            print(name + ' is not in the color list.')
        else:
            if name == 'custom':
                rgb = get_color_tuple()
            else:
                rgb = colors[name]
            print('Color RGB = ' + str(rgb))
            draw_rectangle(canvas, rgb)

    tkinter.mainloop()


if __name__ == '__main__':
    main()
