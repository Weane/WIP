from PIL import Image
from image_editor import ImageEditor

image = Image.open("Plechy.jpg")

editor = ImageEditor(image)

editor.split_image(2)
