import tkinter
import random

CANVAS_WIDTH = 500      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
RADIUS = 5

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

# # You should implement the draw_sketch function below
# def draw_sketch(canvas):
#     nums = int(input("Number of lines in the drawing: "))
#     points = []
#     x, y = random.randint(0, 500), random.randint(0, 300)
#     canvas.create_oval(x-RADIUS/2, y-RADIUS/2, x+RADIUS/2, y+RADIUS/2, outline=COLORS[0], fill=COLORS[0])
#     points.append((x,y))
#     for i in range(1, nums+1):
#         index = i % 6
#         x, y = random.randint(0, 500), random.randint(0, 300)
#         canvas.create_oval(x-RADIUS/2, y-RADIUS/2, x+RADIUS/2, y+RADIUS/2, outline=COLORS[index], fill=COLORS[index])
#         canvas.create_line(points[-1][0], points[-1][1], x, y)
#         points.append((x,y))

def draw_sketch(canvas):
    # num_colors, num_lines, start_x, start_y, centered_circle函数，这里for循环只按num_lines，然后end_x,end_y循环start_x,start_y
    num_colors = len(COLORS)
    num_lines = int(input("Number of lines in the drawing: "))
    start_x = random.randint(0, CANVAS_WIDTH)
    start_y = random.randint(0, CANVAS_HEIGHT)
    centered_circle(canvas, start_x, start_y, RADIUS, COLORS[0])
    
    for i in range(num_lines):
        end_x, end_y = random.randint(0, CANVAS_WIDTH), random.randint(0, CANVAS_HEIGHT)
        centered_circle(canvas, end_x, end_y, RADIUS, COLORS[(i+1)%num_colors])
        canvas.create_line(start_x, start_y, end_x, end_y)
        
        start_x = end_x
        start_y = end_y

def centered_circle(canvas, x, y, radius, color):
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, outline=color, fill=color)
    
def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)   # Assume make_canvas exists
    draw_sketch(canvas)
    tkinter.mainloop()

if __name__ == '__main__':
    main()
