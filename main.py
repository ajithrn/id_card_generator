# Importing the PIL library
from PIL import Image, ImageFont
from PIL import ImageDraw

# Importing the os library to create directories
import os


# Creating output folder if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")


# Functions to open images based on the given input path
def attendee():
    if not os.path.exists("output/attendee"):
        os.makedirs("output/attendee")
    img = Image.open("assets/images/attendee.jpg")
    return img


def sponsor():
    if not os.path.exists("output/sponsor"):
        os.makedirs("output/sponsor")
    img = Image.open("assets/images/sponsor.jpg")
    return img


def organizer():
    if not os.path.exists("output/organizer"):
        os.makedirs("output/organizer")
    img = Image.open("assets/images/organizer.jpg")
    return img


def volunteer():
    if not os.path.exists("output/volunteer"):
        os.makedirs("output/volunteer")
    img = Image.open("assets/images/volunteer.jpg")
    return img

def speaker():
    if not os.path.exists("output/speaker"):
        os.makedirs("output/speaker")
    img = Image.open("assets/images/speaker.jpg")
    return img


# Define a dictionary mapping keys to functions
switch_dict = {
    "attendee": attendee,
    "sponsor": sponsor,
    "organizer": organizer,
    "volunteer": volunteer,
    "speaker": speaker,
}

# Call the function corresponding to a given key
# read text to be inserted to the image
import textwrap
import csv

# Fonts to use
title_font = ImageFont.FreeTypeFont("assets/fonts/DMSans-Bold.ttf", size=85)
comp_font = ImageFont.FreeTypeFont("assets/fonts/DMSans-Bold.ttf", size=55)

# Open CSV file
with open("assets/data/id_data.csv", "r") as file:
    csvreader = csv.reader(file)

    # Skip the first row as it contains the title
    next(csvreader)

    # Iterate through the rows of the file
    for row in csvreader:

        # Get the image corresponding to the attendee type
        img = switch_dict.get(row[3])()

        # Get the width of the image
        width_im = img.size[0]

        # Create an ImageDraw object from the image
        I1 = ImageDraw.Draw(img)

        # Add the attendee name to the image
        astr = (row[0] + " " + row[1]).upper()
        para = textwrap.wrap(astr, width=18)

        # Starting height and padding for the name
        current_h, pad = 2800, 15

        for line in para:
            w = title_font.getlength(line)
            I1.text(
                ((width_im // 2) - (w // 2), current_h),
                line,
                fill=(0, 0, 0),
                font=title_font,
            )
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            I1 = ImageDraw.Draw(img)
            I1.text(
                ((width_im // 2) - (w // 2), current_h),
                line,
                fill=(0, 0, 0),
                font=title_font,
            )
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            I1 = ImageDraw.Draw(img)
            current_h += 95 + pad

        # adding company if exists
        try:
            astr = (row[2]).upper()
            para = textwrap.wrap(astr, width=30)
            current_h += 30

            for line in para:
                w = comp_font.getlength(line)
                I1.text(
                    ((width_im // 2) - (w // 2), current_h ),
                    line,
                    fill=(0, 0, 0),
                    font=comp_font,
                )
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
                I1 = ImageDraw.Draw(img)
                I1.text(
                    ((width_im // 2) - (w // 2), current_h),
                    line,
                    fill=(0, 0, 0),
                    font=comp_font,
                )
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
                I1 = ImageDraw.Draw(img)
                current_h += 65 + pad
        except:
            pass

        # Save the combined image to a file
        # img.convert("CMYK")
        img.save("output/" + row[3] + "/" + row[0] + "_" + row[1] + ".jpg")

file.close()
