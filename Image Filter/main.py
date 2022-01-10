######################################
# Image Filter Project Starter Code  #
#                                    #
#             UTeach CSP             #
#             Brian Ford             #
#                                    #
#              9/20/19               #
#                                    #
######################################


# importing PIL.Image library and os library
from PIL import Image #from PIL import Image 
import os

from PIL.ImageFilter import DETAIL, SHARPEN

# Deletes old created images if they exist
images = ["combinedFilters.jpg","filter1.jpg","filter2.jpg","filter3.jpg","grey.jpg"]
for i in images:
  if os.path.exists(i):
    os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

########################
#    Example Filter    #
########################
def grey():
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (r + g + b) // 3
    newg = (r + g + b) // 3
    newb = (r + g + b) // 3
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage


#####################
#    Your Filter    #
#####################

def filter1():
    # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = r
    newg = g
    newb = b
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # We ask the user how many times they wish to filter the image here, then filter it that many times.
  timesToFilter = -1
  while timesToFilter < 0:
    timesToFilter = int(input("How many times would you like to sharpen the image? "))
    if timesToFilter < 0:
        print ("Invalid input, please enter again.")
  for i in range(int(timesToFilter)):
    newImage = newImage.filter(SHARPEN)
  # And then return it after filtering.
  return newImage


#####################################
#    Your Filters with User Input   #
#####################################

def filter2():
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  changeinR = input ("How much would you like to lower the red value by? ")
  changeinG = input ("How much would you like to lower the green value by? ")
  changeinB = input ("How much would you like to lower the blue value by? ")
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = r - int(changeinR)
    newg = g - int(changeinG)
    newb = b - int(changeinB)
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage

def filter3():
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (r + g + b) // 2
    newg = (r + g + b) // 2
    newb = (r + g + b) // 2
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program, after filtering
  newImage = newImage.filter(DETAIL)
  return newImage

# Creates the four filter images and saves them to our files
a = grey()
a.save("grey.jpg")
b = filter1()
b.save("filter1.jpg")
c = filter2()
c.save("filter2.jpg")
d = filter3()
d.save("filter3.jpg")

# Image filter names for use below
f1 = "filter1"
f2 = "filter2"
f3 = "filter3"

# Apply multiple filters through prompts with the user
answer = input("\nWhich filter do you want me to apply?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
  answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

while answer == "grey" or answer == f1 or answer == f2 or answer == f3:
  if answer == "grey":
   img = grey()
  elif answer == f1:
   img = filter1()
  elif answer == f2:
   img = filter2()
  elif answer == f3:
   img = filter3()
  else:
    break
  print("Filter \"" + answer + "\" applied...")
  answer = input("\nWhich filter do you want me to apply next?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
  while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
    answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
print("Image being created...Done")

# Create the combined filter image and saves it to our files
img.save("combinedFilters.jpg")