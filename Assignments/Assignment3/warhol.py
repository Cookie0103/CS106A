"""
File: warhol.py
---------------
ADD YOUR DESCRIPTION HERE
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

# Name of file that we will use to create the warhol image
IMAGE_FILE = 'Assignments/Assignment3/images/simba.jpg'


def create_filtered_image(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol program. It creates an
    image object from the image in the file IMAGE_FILE, and then recolors the image
    object.  The parameters to this function are:
      red_scale: A number to multiply each pixels' red component by
      green_scale: A number to multiply each pixels' green component by
      blue_scale: A number to multiply each pixels' blue component by
    This function should return a newly generated image with the appropriately
    scaled color values of the pixels.
    """
    image = SimpleImage(IMAGE_FILE)
    for pixel in image:
        pixel.red = min(255, pixel.red * red_scale)
        pixel.blue = min(255, pixel.blue * blue_scale)
        pixel.green = min(255, pixel.green * green_scale)
    return image


def make_warhol():
    """
    This function generates a Warhol-style picture based on the original image in the
    file IMAGE_FILE.  The Warhol image contains "patches" that are different colored
    versions of the original image.  This function returns the Warhol image.
    """
    # width: 222, height: 222
    image_1 = create_filtered_image(1.5, 0, 1.5)
    image_2 = create_filtered_image(0, 1.5, 1.5)
    image_3 = create_filtered_image(1.5, 1.5, 0)
    image_4 = create_filtered_image(0.5, 0.5, 1.5)
    image_5 = create_filtered_image(1.5, 0.5, 0.5)
    image_6 = create_filtered_image(0.5, 1.5, 0.5)
    w, h = image_1.width, image_1.height
    canvas = SimpleImage.blank(width=3*w, height=2*h)
    for y in range(h):
        for x in range(w):
            pixel_1 = image_1.get_pixel(x, y)
            canvas.set_pixel(x, y, pixel_1)
            pixel_2 = image_2.get_pixel(x, y)
            canvas.set_pixel(w+x, y, pixel_2)
            pixel_3 = image_3.get_pixel(x, y)
            canvas.set_pixel(2*w+x, y, pixel_3)
            pixel_4 = image_4.get_pixel(x, y)
            canvas.set_pixel(x, h+y, pixel_4)
            pixel_5 = image_5.get_pixel(x, y)
            canvas.set_pixel(w+x, h+y, pixel_5)
            pixel_6 = image_6.get_pixel(x, y)
            canvas.set_pixel(2*w+x, h+y, pixel_6)
    return canvas


def main():
    """
    This program tests your create_filtered_image and make_warhol functions by calling
    those functions and displaying the resulting images.  Feel free to modify this code
    when you are writing your program.  For example, the call to the create_filtered_image
    function is provided to test that function by itself.  Feel free to delete that portion
    of the code when you have the create_filtered_image working, and then just focus on
    the make_warhol function.
    """
    # single_patch = create_filtered_image(1.5, 0, 1.5)
    # if single_patch != None:
    #     single_patch.show()

    warhol_image = make_warhol()
    if warhol_image != None:
        warhol_image.show()


if __name__ == '__main__':
    main()
