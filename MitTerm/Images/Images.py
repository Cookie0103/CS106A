from simpleimage import SimpleImage

def paste_image(original_img, copy_img, up_x, up_y, low_x, low_y, dest_x, dest_y):
    for y in range(low_y - up_y+1):
        for x in range(low_x - up_x+1):
            if dest_x + x < original_img.width and dest_y + y < original_img.height:
                pixel = copy_img.get_pixel(up_x+x, up_y+y)
                original_img.set_pixel(dest_x+x, dest_y+y, pixel)