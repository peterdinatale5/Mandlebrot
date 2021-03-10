'''
Peter Di Natale
11-02-20
DESCRIPTION: 
In terms of the process for creating the images, I began with the standard (unzoomed) mandlebrot set
that I created for homework. I then went onto the website that was provided to find points on the mandlebrot set
that looked visually appealing, and I chose different points to zoom in on. For my algorthmic zoom, I input
designs/colors into the image based on the "result" or the number of iterations that occured as provided by the
mandlebrot_complex() function. I spent quite some time testing with different colors and designs to see what fit (visually) and what didn't.
I also started with a lot of code that was repetitive, and once I arrived at an appealing image, I organized the code into functions to 
eliminate repition. Lastly, I chose my final fractal: the cantor circles. The most difficult part of drawing this design was arriving 
at the proper way to run the function recursively. I overcame this issue by using notabliltity to sketch out the tasks I was trying to run.

Explanation of fractal and how it is rendered: The fractal I chose esentially creates a circle, and to the left
and right of that circle, there is another circle. (So, every circle has a circle to its left and right side.) This process
continues for a set number of iterations. I rendered this image by halving the diameter of the circle and shifting the
center to the right by a distance that was half the length of the previous diameter. I completed this same algorithm for the left side, 
and when run recursively within the same function, the result was the cantor circle set. The process completed until the diameter 
became a size that was fewer than 2 pixles. I also added a variable passed into the function that controlled the color 
of the circle — I did this to add some variety to the image. In the end, I chose to add a backround of dots that resemble 
stars, since the cantor circles looked like a set of planets to me.

SOURCES: 
https://natureofcode.com/book/chapter-8-fractals/
Note: I used the source above to gain some knowledge about caluculating the cantor circle fractal.

https://www.atopon.org/mandel/#
Note: I used the source above to choose the coordinates to which I zoomed the image in.

HONOR CODE: "On my honor, I have niether given nor recieved unauthorized aid." Peter M. Di Natale
'''
#LIBRARIES
from PIL import Image, ImageDraw
import random

#FUNCTIONS
def mandlebrot_complex(c, z=complex(0,0),iterations=0):
	'''
	This is a fucntion that checks to see if a coordinate "escapes" after repeatedly iterating through the equation. 
	In other words, escaping is either when the max number of iterations is reached, or when |z(sub n+1)| >= 2.
	(This function runs recursively until an escape occurs; then, it returns the number of iterations.)
	'''
	z = z**2 + c #equation for calculating values in mandlebrot set
	iterations = iterations + 1 #increase the number of iterations
	if abs(z) > 2 or iterations > max_iteration-1: #if the coordinate does escape, return the number of iterations
		return iterations
	else: #if the coordinate does not escape, continue with recursing through the function
		return mandlebrot_complex(c, z, iterations)

def img1():
	'''
	Function that calculates the first zoomed in image of the Mandlebrot set.
	Each color parameter (r,g,b for red, green, blue) is the number of iterations
	(determined in the mandlebrot complex function) multiplied by some number. 
	The modulus operator is then used to create a color within the 0-256 color parameter.
	'''
	r = result*3%256 #result is the number of iterations to escape when a complex value "c" is passed into the function "mandlebrot_complex()".
	g = result*5%256
	b = result*8%256
	image1.putpixel((x,y),(r,g,b))

def img2():
	'''
	This function creates another rendering of the mandlebrot set zoomed in at different coordinates.
	The color and pattern are determined by the "result" (number of iterations it took for the coordinate to escape.)
	Within this function, I used the random library to generate some random values for color schemes in addition to 
	some other math. 
	'''
	g = (y*50)*x%256 #variable for green. x*y creates a unique design
	if result > 30 and result <= 100: #range for the green section in img2
		r = result*13%256
		b = random.randint(50,80)
		g = 120
		image2.putpixel((x,y),(r,g,b))
	elif result > 100 and result <= 155: #range for the purple section in img2
		r = 50
		b = random.randint(100,120)
		image2.putpixel((x,y),(g,r,b))
	elif result > 155 and result < 230: #range for the blue section in img2
		r = 180
		b = random.randint(150,170)
		image2.putpixel((x,y),(g,r,b))
	else:#range for the yellow grid in img2
		image2.putpixel((x,y),(x*y,(result*g),100))

def calc_c(xmin, xmax, ymin, ymax): #passing in max and min coordinates (seen in variable section) for zooming in
	'''
	This function iterates through the 1000 x 1000 image and calculates the x and y components of the complex
	portion (c) of the mandlebrot equation. Each time x and y increase, the C value increases by 4/1000. 
	At the end of the function, there is a simple condition to see which img function to run based on the 
	xmin that was passed into calc_c().
	'''
	global x, y, result
	for y in range(imgY): #iterate through the y coordinates
		yc = (((ymax-ymin)/imgY) * y) + ymax #calculating y component of complex number
		for x in range(imgX): # for each y coordinate, iterate through the x coordinates.
			xc = (((xmax-xmin)/imgX) * x) + xmax #calculating x component of complex number
			result = mandlebrot_complex(complex(xc,yc)) #result is the number of iterations when a complex value is passed into the function "mandlebrot_complex()".
			if xmin == -.587083: #this is a condition simply to determine which image function to run
				img1()
			else:
				img2()

def cir(x1, x2, y1, y2, d, c):
	'''
	Function that creates the cantor circles fractal. The process for how this fuction works is described more in depth
	in the description section. But essentially, x1 and x2 are the beginning and end cordinates of the circle, from left to right
	and y1 and y2 are the beginning and end coordinates of the circle from top to bottom. d is a variable that I use to determine the diameter
	of the circle, and each time the function recurses, the variable halves. (In the first circle, d is the distance from each point 
	(x1,x2,y1, and y2) to the edge of the 1000x1000 image frame.) The math and testing behind this variable was determined through lots of 
	drawing/calculations in notability.

	'''
	shape = [(x1,y1), (x2, y2)] #parameters for the ellipse
	colors = ["orange", "red", "blue", "magenta", "yellow", "brown", "green", "red"] #color list
	img1 = ImageDraw.Draw(image3)
	color = colors[c] #list of colors that the function will iterate through using the "c" value
	img1.ellipse(shape, outline = color) #drawing the ellipse and setting the outline to a color
	if d > 2:
		'''
		For each of the lines below, the distance between the y coordinates decreases at the same rate (dividing by 4).
		The distance between the x coordinates when drawing circles to the left and to the right also decrease at the same rate, 
		but (as seen below in the first two parameters) the fractions are inverses of each other depending on whether the circle 
		is being drawn to the left or to the right. The specific ratios were determined through after several iterations of testing, 
		drawing in notability, and basic fraction calculations.
		'''
		cir(x1-d/2, (x2-(d*3/2)), y1+((y2-y1)/4), y2-((y2-y1)/4), d/2, c+1)#drawing circles to the right (general math explained above)
		cir(x1+d*3/2, (x2+(d/2)), y1+((y2-y1)/4), y2-((y2-y1)/4), d/2, c+1)#drawing circles to the left (general math explained above)

def cir_backround(r,g,b):
	# Fucntion that creates dots as a backdrop for the cantor circle fractal
	# I chose dots specifically because they resemble stars, as this fractal kind of looks like a set of planets to me!
	for x in range(0,imgX,10): #iterating through x coordinates at a step of 10
		for y in range(0,imgY,10): #iterating through y coordinates at a step of 10 (for each x coordinate)
				image3.putpixel((x,y),(r,g,b))

#VARIABLES
imgX = 1000 #img width
imgY = 1000 #img height
d = 250 #d variable for determining the diameter (explained in cir() description)
max_iteration = 255

#setting parameters for images 1,2, and 3, including RGB color scheme and dimensions
image1 = Image.new("RGB",(imgX, imgY)) 
image2 = Image.new("RGB",(imgX, imgY))
image3 = Image.new("RGB", (imgX, imgY))

#coordinates for first mandlebrot set zoom
xmin_1 = -.587083
xmax_1 = -.453333
ymin_1 = .474166
ymax_1 = .597916

#coordinates for second mandlebrot set zoom
xmin_2 = -0.934
xmax_2 = -0.929
ymin_2 = 0.247
ymax_2 = 0.253

#MAIN CODE
calc_c(xmin_1, xmax_1, ymin_1, ymax_1)
image1.save("img1.png", "PNG") #saving image as a png (same for other two images below)

calc_c(xmin_2, xmax_2, ymin_2, ymax_2)
image2.save("img2.png", "PNG")

cir_backround(0,180,0) #(I set the function up so I could pass in numbers for colors to make testing more simplified)
cir(d,(imgX/2)+d,d,(imgY/2)+d, d, 0)
image3.save("img3.png", "PNG")


'''
FEEDBACK: 
FROM MAX Z.: 
- Change the coloring of the circles in the last image to make it more exciting
Based on this feedback, I passed through a list of different colors to change the outline color
of my circle. This method used a variable that was passed into the function and decreased each time through.

FROM MS. HEALEY: 
- Make the method of coloring the mandle zoom less similar than that of the first image.
To diversify the images, I did a few things. First, I used the random library to choose a number that I would
use as a color parameter. I also added more intervals in terms of the number of iterations, which helped create
more distinct coloring. Within these intervals, I either used the random library, some math, or just a basic 
number to decide on the color/pattern of specific section. These values were then organized in variables.
- Make the circle fractal design go to the edges of the 1000x1000 image.
I was also able to accomplish this by changing the value of d, as mentioned above. Using some math in notability, 
I had to figure out how far out the circles would extend, then I took that d value to determine the appropriate value
of the diameter of the initial circle; recursion handled the rest.
'''
