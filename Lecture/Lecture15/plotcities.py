"""
File: plotcities.py
-------------------
This program plots the location of cities in the US from a file
of city longitude and latitude coordinates.
"""

import tkinter

# Make the window large so that we can see more detail. 
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600

# The viewpoint coordinates - the min and max longitude and latitude
MIN_LONGITUDE = -130
MAX_LONGITUDE = -60
MIN_LATITUDE = +20
MAX_LATITUDE = +55


def main():
	# get a drawing canvas
	canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

	# load the file
	with open('us-cities.txt', encoding="utf-8") as cities_file:

		# skip the first line, its just a header
		next(cities_file)

		# read the file one line at a time
		for line in cities_file:
			line = line.strip()			# get rid of all the whitespace
			parts = line.split(',')		# split the line into list of parts
			# parts = [city, state, latitude, longitude]
			lat = float(parts[2])		# get latitude as a numeric value
			lon = float(parts[3])		# get longitude as a numeric value
			plot_one_city(canvas, lat, lon)

		canvas.mainloop()


def plot_one_city(canvas, latitude, longitude):
	"""
	Given the longitude and latitude of a city (in double form), displays
	a dot for that city.
	"""
	x = longitude_to_x(longitude)
	y = latitude_to_y(latitude)
	plot_pixel(canvas, x, y)


def plot_pixel(canvas, x, y):
	"""
	Plots a pixel (1x1 rectangle) at the specified (x, y) coordinate.
	"""
	canvas.create_rectangle(x, y, x+1, y+1, fill="blue", outline="blue")


def longitude_to_x(longitude):
	"""
	Given a raw longitude, returns the screen x coordinate where
	it should be displayed.
	"""
	return CANVAS_WIDTH * (longitude - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)


def latitude_to_y(latitude):
	"""
	Given a raw latitude, returns the screen y coordinate where
	it should be displayed.
	"""
	return CANVAS_HEIGHT * (1.0 - ((latitude - MIN_LATITUDE) / (MAX_LATITUDE - MIN_LATITUDE)))


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
	"""
	DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
	top = tkinter.Tk()
	top.minsize(width=width + 10, height=height + 10)
	top.title('graphics')
	canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
	canvas.pack()
	canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
	canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
	return canvas


if __name__ == '__main__':
	main()
