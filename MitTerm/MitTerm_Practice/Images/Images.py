from simpleimage import SimpleImage

def create_blurred_image(img):
    width = img.width
    height = img.height
    image = SimpleImage.blank(width=width, height=height)
    for y in range(height):
        for x in range(width):
            pixel_new = image.get_pixel(x, y)
            avg_pixel = cal_average(img, x, y, pixel_new)
            image.set_pixel(x, y, avg_pixel)
    return image


def cal_average(img, x, y, pixel_new):
    width = img.width
    height = img.height
    pixel_list = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if x+i>=0 and x+i<width and y+j>=0 and y+j<height:
                pixel = img.get_pixel(x+i, y+j)
                pixel_list.append(pixel)
    avg_pixel = cal_pixel_avg(pixel_list, pixel_new)
    return avg_pixel


def cal_pixel_avg(pixel_list, pixel_new):
    red, green, blue = 0, 0, 0
    for pixel in pixel_list:
        red += pixel.red
        blue += pixel.blue
        green += pixel.green
    pixel_new.red = red / len(pixel_list)
    pixel_new.green = green / len(pixel_list)
    pixel_new.blue = blue / len(pixel_list)
    return pixel_new

my_image = SimpleImage("D:\项目\CS106A\MitTerm\Images\stop.png")
my_image.show()
image = create_blurred_image(my_image)
image.show()