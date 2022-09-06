import os
import textwrap
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class MemeEngine:
    """ This class is going to be responsible for loading the image, manipulating and drawing text on to the image
     and saving the manipulated image.
     """
    def __init__(self, file_dir):
        """Output directory path is set up as an instance object."""
        self.file_dir = file_dir
        self.count = 1
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    def make_meme(self, img_path, text, author, width=500):
        """ The meme is created with the given image, text and author"""
        with Image.open(img_path) as img:
            true_width, true_height = img.size
            height = int(true_height * width/ true_width)
            ALT_SIZE = (width, height)
            img.thumbnail(ALT_SIZE)

            """The selected font that the text on the image will be displayed as."""
            fnt1 = ImageFont.truetype("./_data/Fonts/impact.ttf", 29)
            fnt2 = ImageFont.truetype("./_data/Fonts/impact.ttf", 25)

            """The x and y coordinates representing the position the text will be on the image."""
            x_pos = 30
            y_pos = 25

            """A tuple representing the x and y position."""
            xy_COORD = (x_pos, y_pos)

            """The text color and outline added to a dictionary of attributes to be used later"""
            fill = (255, 255, 255)
            stroke_color = (0, 0, 0)
            attributes = {'fill': (255, 255, 255), 'font': fnt1, 'stroke_width': 1, 'stroke_fill': (0, 0, 0)}

            """The text drawn on the image."""
            d = ImageDraw.Draw(img)
            word_list = textwrap.TextWrapper(width=25).wrap(text)
    
            for element in word_list:
                    d.text((x_pos, y_pos), element, **attributes)
                    y_pos += 35
            d.text((x_pos,  y_pos + 25), f"- {author}", fill, fnt2, stroke_width=1, stroke_fill=stroke_color)
    
            """The resulting image file path is returned."""
            outfile = os.path.join(self.file_dir, f"temp-{self.count}.jpg")
            self.count += 1
            img.save(outfile, "JPEG")
            return outfile

   