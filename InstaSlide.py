import json
from PIL import Image, ImageDraw, ImageFont

# load parameters from JSON file
with open('parameters.json') as f:
    parameters = json.load(f)

# set image size and font properties
image_width = 1080
image_height = 1080
font_size = 60
font = ImageFont.truetype('arial.ttf', font_size)

# create a new image for each set of parameters
for i, parameter_set in enumerate(parameters):
    # create a new image with the desired size and color
    image = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))

    # create a draw object for the image
    draw = ImageDraw.Draw(image)

    # calculate the position for the title
    title_x = (image_width - font.getsize(parameter_set['title'])[0]) / 2
    title_y = image_height / 3 - font_size / 2

    # calculate the position for the tip
    tip_x = (image_width - font.getsize(parameter_set['tip'])[0]) / 2
    tip_y = image_height / 3 + font_size / 2

    # calculate the position for the website
    website_x = (image_width - font.getsize(parameter_set['website'])[0]) / 2
    website_y = 2 * image_height / 3 - font_size / 2

    # calculate the position for the Instagram username
    ig_username_x = (image_width - font.getsize('@' + parameter_set['ig_username'])[0]) / 2
    ig_username_y = 2 * image_height / 3 + font_size / 2

    # add the title, tip, website, and Instagram username to the image
    draw.text((title_x, title_y), parameter_set['title'], font=font, fill=(0, 0, 0))
    draw.text((tip_x, tip_y), parameter_set['tip'], font=font, fill=(0, 0, 0))
    draw.text((website_x, website_y), parameter_set['website'], font=font, fill=(0, 0, 0))
    draw.text((ig_username_x, ig_username_y), '@' + parameter_set['ig_username'], font=font, fill=(0, 0, 0))

    # save the image to a file
    image.save('slide{}.png'.format(i+1))