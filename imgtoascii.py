from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")  

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return
    
    image = resize_image(image, new_width)
    image = grayscale_image(image)

    ascii_str = map_pixels_to_ascii(image)
    
    ascii_img = "\n".join([ascii_str[i:(i + new_width)] for i in range(0, len(ascii_str), new_width)])
    return ascii_img

image_path = "image.jpg"  # Replace with the path to your image
ascii_art = convert_image_to_ascii(image_path, new_width=100)
with open("ggg.txt", 'w+') as img:
    img.write(ascii_art)
