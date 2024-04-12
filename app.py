#author Ashley Chiteri
from PIL import Image

#ascii characters with descending order of intensity
chars = ["@", "#", "s", "%", "?", "*", "+", ";", ":", ",", "."]

#resizing the image
def resize_image(img, new_width=120):
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_img = img.resize((new_width, new_height))
    return(resized_img)

#convert the image to a greyscale
def greysify(img):
    greyscale_image = img.convert("L")
    return(greyscale_image)

#converting pixels to ascii characters
def pixels_to_ascii(img):
    pixels = img.getdata()
    characters = "".join([chars[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=120):
    #getting an image form the user
    path = input("Enter the path of the image: \n")

    #trying to load the image using exceptions
    try:
        img = Image.open(path)

    except:
        print(path, "could not find the image")

    #list of ascii characters
    new_image_data = pixels_to_ascii(greysify(resize_image(img)))

    #get the length of the list of characters
    pixel_count = len(new_image_data)

    #splitting the chars to equal lenghts
    ascii_image = "\n".join(new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width))

    #printing the results
    print(ascii_image)

    # save the results to a file
    with open('sample_ascii_image.txt',"w") as f:
        f.write(ascii_image)

main()
