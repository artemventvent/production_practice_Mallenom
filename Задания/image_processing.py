from PIL import Image
import os


def convert_to_grayscale(image_path):
    img = Image.open(image_path).convert('L')
    grayscale_path = os.path.splitext(image_path)[0] + '_grayscale.png'
    img.save(grayscale_path)
    return grayscale_path