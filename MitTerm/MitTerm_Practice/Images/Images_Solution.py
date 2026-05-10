from simpleimage import SimpleImage

def create_blurred_image(img, blur, x, y):
    # 计算num_pixels个数，红绿蓝大小，然后遍历[-1,0,1]，直接从blur
    num_pixels = 0
    red, green, blue = 0, 0, 0
    for col in range(x-1, x+2):
        for row in range(y-1, y+2):
            if col>=0 and col<img.width and row>=0 and row<img.height:
                num_pixels += 1
                red += img.get_pixel(col, row).red
                green += img.get_pixel(col, row).green
                blue += img.get_pixel(col, row).blue
    blur_pixel = blur.get_pixel(x, y)
    blur_pixel.red = red // num_pixels
    blur_pixel.green = green // num_pixels
    blur_pixel.blue = blue // num_pixels

def create_blurred_image(img):
    # 创建blur直接遍历
    height = img.height
    width = img.width
    
    blur = SimpleImage.blank(width=width, height=height)
    
    for y in range(height):
        for x in range(width):
            blur_pixel = create_blurred_image(img, blur, x, y)
            blur.set_pixel(x, y, blur_pixel)
    return blur

my_image = SimpleImage("D:\项目\CS106A\MitTerm\Images\stop.png")
my_image.show()
image = create_blurred_image(my_image)
image.show()