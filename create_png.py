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

        # Get the width and height of the image
        width, height = image.size

        if 'ObjectWidth' in obj_location:
            if '%' in obj_location['ObjectWidth']:
                obj_width = int(float(obj_location['ObjectWidth'].strip('%'))/100 * template_width)
                if 'ObjectHeight' in obj_location:
                    if '%' in obj_location['ObjectHeight']:
                        obj_height = int((float(obj_location['ObjectHeight'].strip('%')))/100 * template_height)
                    elif str(obj_location['ObjectHeight']).digit():
                        obj_height = int(float(obj_location['ObjectHeight'])/pxToMillConv)
                    else:
                        obj_height = int(height)
                else:
                    obj_height = int(float(obj_width/width)*height)
            elif str(obj_location['ObjectWidth']).isdigit():
                obj_width = int(float(obj_location['ObjectWidth'])/pxToMillConv)
                if 'ObjectHeight' in obj_location:
                    if '%' in obj_location['ObjectHeight']:
                        obj_height = int((float(obj_location['Objectheight'].strip('%')))/100 * template_height)
                    elif str(obj_location['ObjectHeight']).isdigit():
                        obj_height = int(float(obj_location['ObjectHeight'])/pxToMillConv)
                    else:
                        obj_height = int(height)
            else:
                obj_width = int(width)
                if 'ObjectHeight' in obj_location:
                    if '%' in obj_location['ObjectHeight']:
                        obj_height = int(float(obj_location['Objectheight'].strip('%'))/100 * template_height)
                    elif str(obj_location['ObjectHeight']).isdigit():
                        obj_height = int(float(obj_location['ObjectHeight'])/pxToMillConv)
                    else:
                        obj_height = int(height)
        elif 'ObjectHeight' in obj_location:
            if '%' in obj_location['ObjectHeight']:
                obj_height = int(float(obj_location['ObjectHeight'].strip('%'))/100 * template_height)
            elif str(obj_location['ObjectHeight']).isdigit():
                obj_height = int(float(obj_location['ObjectHeight'])/pxToMillConv)
            else:
                obj_height = int(height)
        else:
            obj_height = int(height)
            obj_width = int(width)




        

        # Print the width of the image
        print(obj_height)
        print(obj_width)

        if 'ObjectXOffset' in obj_location:
            if '%' in obj_location['ObjectXOffset']:
                obj_x_offset = int((float((obj_location['ObjectXOffset'].strip('%')))/100 * template_width)-(obj_width/2))
            elif str(obj_location['ObjectXOffset']).isdigit():
                obj_x_offset = int(float(obj_location['ObjectXOffset'])/pxToMillConv)
            else:
                obj_x_offset = 0
        else:
            obj_x_offset = 0
        if 'ObjectYOffset' in obj_location:
            if '%' in obj_location['ObjectYOffset']:
                obj_y_offset = int((float((obj_location['ObjectYOffset'].strip('%')))/100 * template_height)-(obj_height/2))
            elif str(obj_location['ObjectYOffset']).isdigit():
                obj_y_offset = int(float(obj_location['ObjectYOffset'])/pxToMillConv)
            else:
                obj_y_offset = 0
        else:
            obj_y_offset = 0

        # Resize the image to the specified dimensions
        image = image.resize((obj_width, obj_height), Image.ANTIALIAS)

        # Paste the image onto the template image at the specified location
        template_image.paste(image, (obj_x_offset, obj_y_offset, obj_x_offset + obj_width, obj_y_offset + obj_height))

         



    elif obj_type == 'Text':
        # Get the object dimensions
        obj_width = int(float(obj_location['ObjectWidth'])/pxToMillConv)
        obj_height = int(float(obj_location['ObjectHeight'])/pxToMillConv)
        # obj_x_offset = int(float(obj_location['ObjectXOffset'])/pxToMillConv)
        # obj_y_offset = int(float(obj_location['ObjectYOffset'])/pxToMillConv)

        # Load the TTF font file
        font_path = obj_content['Font']
        font = ImageFont.truetype(font_path, int(float(obj_content['FontSize'])/pxToMillConv))

        # Get the font color
        font_color = tuple(int(obj_content['FontColor'][i:i+2], 16) for i in (0, 2, 4))

        text_width, text_height = font.getsize(obj_content['Text'])
        print(text_width)
        print(text_height)

        # Get the height of the smallest character in the text
        text = obj_content['Text']
        char_heights = []
        for char in text:
            char_width, char_height = font.getsize(char)
            char_heights.append(char_height)
            print(f'The height of the {char} character is {char_height} pixels.')
        min_char_height = min(char_heights)

        print(f'The height of the smallest character is {min_char_height} pixels.')


        if 'ObjectXOffset' in obj_location:
            if '%' in obj_location['ObjectXOffset']:
                obj_x_offset = int((float((obj_location['ObjectXOffset'].strip('%')))/100 * template_width)-(text_width/2))
            elif str(obj_location['ObjectXOffset']).isdigit():
                obj_x_offset = int(float(obj_location['ObjectXOffset'])/pxToMillConv)
            else:
                obj_x_offset = 0
        else:
            obj_x_offset = 0
        if 'ObjectYOffset' in obj_location:
            if '%' in obj_location['ObjectYOffset']:
                obj_y_offset = int((float((obj_location['ObjectYOffset'].strip('%')))/100 * template_height)-(min_char_height/2))
            elif str(obj_location['ObjectYOffset']).isdigit():
                obj_y_offset = int(float(obj_location['ObjectYOffset'])/pxToMillConv)
            else:
                obj_y_offset = 0
        else:
            obj_y_offset = 0

        # Draw the text onto the image
        draw.text((obj_x_offset, obj_y_offset), obj_content['Text'], fill=font_color, font=font)
        print("_")
        print(obj_x_offset*pxToMillConv)
        print(obj_y_offset*pxToMillConv)

       


# Save the image as a PNG file
template_image.save('template.png', dpi=(300, 300))


