"""
File: ghost.py
--------------
YOUR DESCRIPTION HERE
"""

import os
import sys

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 0, 255)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """
    pred, pgreen, pblue = pixel.red, pixel.green, pixel.blue
    diff = (pred - red)**2 + (pgreen - green)**2 + (pblue - blue)**2
    return diff


def get_best_pixel(pixel_list):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across
    all pixels.

    Input:
        a list of pixels to be averaged and compared.  You can assume this list is never empty
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel([green_pixel, green_pixel, blue_pixel])
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel([red_pixel, red_pixel, red_pixel])
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """
    avg_red, avg_green, avg_blue = cal_avg_pixel(pixel_list)
    closest = float('inf')
    for p in pixel_list:
        dist = get_pixel_dist(p, avg_red, avg_green, avg_blue)
        if dist <= closest:
            closest = dist
            best_pixel = p
    return best_pixel

def cal_avg_pixel(pixel_list):
    pred, pblue, pgreen = 0, 0, 0
    for p in pixel_list:
        pred += p.red
        pblue += p.blue
        pgreen += p.green
    avg_red = pred // len(pixel_list)
    avg_blue = pblue // len(pixel_list)
    avg_green = pgreen // len(pixel_list)
    return avg_red, avg_green, avg_blue

def create_ghost(image_list):
    """
    Given a list of image objects, this function creates and returns a Ghost
    solution image based on the images passed in. All the images passed
    in will be the same size.

    Input:
        a list images to be processed.  You can assume this list is never empty.
    Returns:
        a new Ghost solution image
    """
    width, height = image_list[0].width, image_list[0].height
    image = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel_list = []
            for i in image_list:
                pixel = i.get_pixel(x, y)
                pixel_list.append(pixel)
            best_pixel = get_best_pixel(pixel_list)
            image.set_pixel(x, y, best_pixel)
            # print(best_pixel.red, best_pixel.green, best_pixel.blue)
            # print(pixel.red, pixel.green, pixel.blue)
    return image

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images)
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")


if __name__ == '__main__':
    main()
