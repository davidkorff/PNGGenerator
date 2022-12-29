import json
from PIL import Image, ImageDraw, ImageFont



pxToMillConv = 0.084666667

# Open the JSON file and read the contents
with open('Art.json') as f:
    data = json.load(f)



# Get the dimensions of the template image from the "MaxTemplate" object
template_width = int(float(data['Template']['MaxTemplate']['Width'])/pxToMillConv)
template_height = int(float(data['Template']['MaxTemplate']['Height'])/pxToMillConv)

# Create a new image with the specified dimensions and a transparent background
template_image = Image.new(mode='RGBA', size=(template_width, template_height), color = (255, 255, 255, 0))

# Create a drawing context for the image
draw = ImageDraw.Draw(template_image)

# Iterate over the personalized objects
for personalized_object in data['Template']['PersonalizedObjects']:
    obj = personalized_object['PersonalizedObject']
    obj_type = obj['ObjectType']
    obj_content = obj['ObjectContent']
    obj_location = obj['ObjectLocation']

    # Get the object dimensions and offsets
    obj_width = int(float(obj_location['ObjectWidth'])/pxToMillConv)
    obj_height = int(float(obj_location['ObjectHeight'])/pxToMillConv)
    obj_x_offset = int(float(obj_location['ObjectXOffset'])/pxToMillConv)
    obj_y_offset = int(float(obj_location['ObjectYOffset'])/pxToMillConv)

    if obj_type == 'IMG':
        # Open the image file
        import requests

        # Download the image from the URL
        response = requests.get(obj_content['imageURL'])

        # Save the image to a local file
        with open('image.png', 'wb') as f:
            f.write(response.content)

        # Open the local image file
        image = Image.open('image.png')

        # Resize the image to the specified dimensions
        image = image.resize((obj_width, obj_height), Image.ANTIALIAS)

        # Paste the image onto the template image at the specified location
        template_image.paste(image, (obj_x_offset, obj_y_offset, obj_x_offset + obj_width, obj_y_offset + obj_height))
    elif obj_type == 'Text':
        # Load the TTF font file
        font_path = 'arial.ttf'
        font = ImageFont.truetype(font_path, int(float(obj_content['FontSize'])))

        # Get the font color
        font_color = tuple(int(obj_content['FontColor'][i:i+2], 16) for i in (0, 2, 4))

        # Draw the text onto the image
        draw.text((obj_x_offset, obj_y_offset), obj_content['Text'], fill=font_color, font=font)

# Save the image as a PNG file
template_image.save('template.png', dpi=(300, 300))


