import json, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# load parameters from JSON file
with open('parameters.json') as f:
    parameters = json.load(f)

# set image size and font properties
image_width = 1080
image_height = 1080
tip_font_size = 35
font_size = 60
font = ImageFont.truetype('arial.ttf', font_size)

# create a new image for each set of parameters
for i, parameter_set in enumerate(parameters):
    # create a new image with the desired size and color
    image = Image.new('RGB', (image_width, image_height), color=(0, 0, 0))

    # create a draw object for the image
    draw = ImageDraw.Draw(image)

    # calculate the position for the title
    title_x = (image_width - font.getsize(parameter_set['title'])[0]) / 2
    title_y = image_height / 3 - font_size / 2 -250

    # calculate the position for the tip
    tip_lines = textwrap.wrap(parameter_set['tip'], width=30) # wrap tip text into multiple lines
    tip_x = (image_width - font.getsize(tip_lines[0])[0]) / 2
    tip_y = image_height / 3 + tip_font_size / 2 + -200 #positioning tip description

    for line in tip_lines:
        print(line)
        draw.text((tip_x, tip_y), line, font=font, fill=(255, 255, 255))
        tip_y += tip_font_size + tip_font_size/2

    # calculate the position for the website
    website_x = (image_width - font.getsize(parameter_set['website'])[0]) / 2
    website_y = 2 * image_height / 3 - font_size / 2

    # calculate the position for the Instagram username
    ig_username_x = (image_width - font.getsize('@' + parameter_set['ig_username'])[0]) / 2
    ig_username_y = 2 * image_height / 3 + font_size / 2

    # add the title, tip, website, and Instagram username to the image
    draw.text((title_x, title_y), parameter_set['title'], font=font, fill=(255, 255, 255)) #you might have to tweak the colors of your text depending on the background color you pick
    draw.text((website_x, website_y+220), parameter_set['website'], font=font, fill=(255, 255, 255))
    draw.text((ig_username_x, ig_username_y +250), '@' + parameter_set['ig_username'], font=font, fill=(255, 255, 255))
    


    # save the image to a file
    image.save('slide{}.png'.format(i+1))
    
    #add profile photo to the slide
    im1 = Image.open('slide{}.png'.format(i+1))
    im2 = Image.open('photo.png') #add your profile photo here that you want to appear in the slide
    mask_im = Image.new("L", im2.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((100, -10, 460, 400), fill=255) #You might have to tweak the position and size a bit depending on your photo
    mask_im.save('mask_circle.png'.format(i+1), quality=100)

    mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
    mask_im_blur.save('mask_circle_blur.jpg', quality=100)

    back_im = im1.copy()
    back_im.paste(im2, (300, 500), mask_im_blur)
    #overwrite the slides with your profile pictures inside them
    back_im.save('slide{}.png'.format(i+1), quality=100)