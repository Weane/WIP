from PIL import Image
import os


class ImageEditor:
    def __init__(self, image):
        self.image = image

    def split_image(self, number_of_parts):
        width, height = self.image.size
        part_size = width // number_of_parts
        for part_number in range(number_of_parts):
            start_point = part_size * part_number
            box = (start_point, 0, start_point + part_size, height)
            self.image.crop(box).save(self.find_free_filename(self.image.filename.split(".")[0], self.image.filename.split(".")[1]))
            print(f"{box} {part_number} {part_size}x{height}")

    def find_free_filename(self, filename, extension, i=1):
        """
        Searching for free filename and trying to add _ and number at the end of the filename.
        :param filename - name of the file
        :param extension - type of file
        :param i - number to add at the end of filename default is 1
        :return:
        """
        new_filename = f"{filename}_{i}.{extension}"
        if not os.path.exists(new_filename):
            return new_filename
        return self.find_free_filename(filename, extension, i + 1)
