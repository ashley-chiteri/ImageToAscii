#author Ashley Chiteri
from PIL import Image

path = input("Enter the path of the image: \n")

#trying to load the image using exceptions
try:
    img = Image.open(path)

except:
    print(path, "could not the image")

#RESIZING the image to reduce chaos
width, height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))

#convert the image to a greyscale
img = img.convert("L")

#a list of the ascii characters from darkests to lightest
chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]

pixels = img.getdata()
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

#splitting the chars to equal lenghts
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)

print(ascii_image)

#we can display it on a file
with open('sample_ascii_image.txt',"w") as f:
    f.write(ascii_image)
