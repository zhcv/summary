#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import os
from string import Template
from PIl import Image
from PIL import ImageFilter

parser = argparse.ArgumentParser(descreption='Convert images to 16:9 aspect ratio
                                 with blurred sidebars')
parser.add_argument('path', metavar='path', help='Directory where lo load images')


def landscapeDimensions(size):
    width, height = size
    width = int(height * 16.0 / 9)
    return width, height

def blurImage(imagePath):
    ext = ('.jpg', '.gif', '.png', '.tga', '.bmp')
    image_paths = [os.path.join(imagePath, f) for f in os.listdir(imagePath) 
                   if f.endswith(ext)]
    for image_path in image_paths:
        # Read image
        background = Image.open(image_path)
        new_dimensions = landscapeDimensions(background.size)
        resized_background = background.resize(new_dimensions)

        # Applying a filter to the image
        im_blur = resized_background.filter(ImageFilter.GaussianBlur(radius = 30))
        foreground = Image.open(image_path)
        width, height = foreground.size
        new_width, _ = new_dimensions
        x_offset = int((new_width - width) / 2)
        im_blur.paste(foreground, (x_offset, 0))

        base_filename = os.path.basename(image_path)
        template = Template('_processed_$base_filename')
        filename = template.substitute(base_filename=base_filename)
        # saving the filtered image to a new file
        im_blur.save(os.path.join(imagePath, filename))

if __name__ == '__main__':
    args = parser.parse_args()
    blurImage(args.path)
