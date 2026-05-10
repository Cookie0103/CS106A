"""
File: showblend.py
------------------
This program shows the user, graphically, the amount of red, green, and blue
in a color.
"""

import tkinter


CANVAS_WIDTH = 600                      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300                     # Height of drawing canvas in pixels
RECTANGLE_WIDTH = 100                   # Width of color rectangle in pixels
RECTANGLE_HEIGHT = 50                   # Height of color rectangle in pixels
SPACE = 20                              # Space between color squares in pixels
COLORFILE = 'data/ColorRGB.csv'         # File of color names and rgb values


def load_colors(filename):
    """
    Loads colors from a comma separated value file where each
    line defines a color based on RGB values, as follows:
    <color name>, <red>, <green>, <blue>
    Returns a dictionary with color names as keys and RGB values in a list.
    """
    color_dict = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split(',')
            color_name = parts[0]
            rgb_list = []
            for i in range(1, 4):
                rgb_list.append(int(parts[i]))
            color_dict[color_name] = rgb_list
    return color_dict


def list_colors(colors):
    """
    Lists all the colors in the dictionary of colors -> RGB values passed in
    """
    print("List of all color names:")
    for color in colors:
        print(color)


def color_from_rgb(rgb_list):
    """
    Given a list of RGB values, this function creates and returns a
    hexadecimal string of RGB colors (#RRGGBB) that can be used for drawing
    """
    hex_red = "%02x" % rgb_list[0]
    hex_green = "%02x" % rgb_list[1]
    hex_blue = "%02x" % rgb_list[2]
    hex_color = "#" + hex_red + hex_green + hex_blue
    return hex_color


def show_blend(canvas, rgb_list):
    """
    Draws a set of rectangles on the canvas, to show both color determined by the
    list of RGB values passed in, as well as the red, green, and blue channels
    separately.
    """
    full_color = color_from_rgb(rgb_list)

    # Draws scaled rectangles to show amount of color of each R, G, B channel
    canvas.create_rectangle(SPACE, SPACE,
                            SPACE + ((rgb_list[0] / 255) * RECTANGLE_WIDTH), SPACE + RECTANGLE_HEIGHT,
                            fill='red', outline='red')

    canvas.create_rectangle(SPACE, (2 * SPACE) + RECTANGLE_HEIGHT,
                            SPACE + ((rgb_list[1] / 255) * RECTANGLE_WIDTH), 2 * (SPACE + RECTANGLE_HEIGHT),
                            fill='green', outline='green')

    canvas.create_rectangle(SPACE, (3 * SPACE) + (2 * RECTANGLE_HEIGHT),
                            SPACE + ((rgb_list[2] / 255) * RECTANGLE_WIDTH), 3 * (SPACE + RECTANGLE_HEIGHT),
                            fill='blue', outline='blue')

    # Draw full color rectangle
    canvas.create_rectangle((2 * SPACE) + RECTANGLE_WIDTH, (2 * SPACE) + RECTANGLE_HEIGHT,
                            2 * (SPACE + RECTANGLE_WIDTH), 2 * (SPACE + RECTANGLE_HEIGHT),
                            fill=full_color, outline=full_color)


def make_canvas(width, height):
    """
    Creates and returns a drawing canvas of the given width
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
        elif name not in colors.keys():
            print(name + ' is not in the color list.')
        else:
            canvas.delete('all')
            rgb = colors[name]
            print('Color RGB = ' + str(rgb))
            show_blend(canvas, rgb)

    tkinter.mainloop()


if __name__ == '__main__':
    main()
