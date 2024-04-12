#author Ashley Chiteri
from PIL import Image

#ascii characters with descending order of intensity
chars = ["@", "#", "s", "%", "?", "*", "+", ";", ":", ",", "."]

#resizing the image
def resize_image(img, new_width=100):
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_img = img.resize((new_width, new_height))
    return(resized_img)

#convert the image to a greyscale

def main():
    #getting an image form the user
    path = input("Enter the path of the image: \n")

    #trying to load the image using exceptions
    try:
        img = Image.open(path)

    except:
        print(path, "could not the image")

main()


img = img.convert("L")



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
