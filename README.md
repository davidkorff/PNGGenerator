#extractor.py
This script extracts a JSON object from a URL and saves it to a file named Art.json.

To use this script, you will need to provide the URL as a command-line argument. For example:

'''
python extractor.py "https://example.com?template={'key':'value'}"
'''

The JSON object must be passed as the value of the template query parameter in the URL.

#create_png.py
This script reads a JSON object from a file named Art.json and generates a PNG image from it. The image will be saved to a file named template.png.

The JSON object is expected to contain a dictionary with the following structure:

'''
{
  "Template": {
    "MaxTemplate": {
      "Width": "1000",
      "Height": "1000"
    },
    "PersonalizedObjects": [
      {
        "PersonalizedObject": {
          "ObjectType": "IMG",
          "ObjectContent": {
            "imageURL": "https://example.com/image.png"
          },
          "ObjectLocation": {
            "ObjectWidth": "500",
            "ObjectHeight": "500",
            "ObjectXOffset": "250",
            "ObjectYOffset": "250"
          }
        }
      },
      {
        "PersonalizedObject": {
          "ObjectType": "Text",
          "ObjectContent": {
            "Text": "Hello, World!",
            "FontSize": "36",
            "FontColor": "000000"
          },
          "ObjectLocation": {
            "ObjectWidth": "500",
            "ObjectHeight": "500",
            "ObjectXOffset": "250",
            "ObjectYOffset": "250"
          }
        }
      }
    ]
  }
}
'''

The `MaxTemplate` object specifies the dimensions of the resulting image. The PersonalizedObjects list contains objects that will be added to the image. Each object can be either an image (specified with the `IMG` `ObjectType`) or text (specified with the `Text` `ObjectType`).

The `ObjectContent` object for an image object should contain an `imageURL` field with the URL of the image to be added to the image.

The `ObjectContent` object for a text object should contain a `Text` field with the text to be added to the image, a `FontSize` field with the font size in pixels, and a `FontColor` field with the font color in hexadecimal format.

The `ObjectLocation` object specifies the dimensions and position of the object on the image. The `ObjectWidth` and `ObjectHeight` fields specify the dimensions of the object in pixels, and the `ObjectXOffset` and `ObjectYOffset` fields specify the distance from the top-left corner of the image to the top-left corner of the object.

The script will read the JSON object and create an image with a transparent background. It will then iterate over the `PersonalizedObjects` list and add each object to the image. If the object is an image, it will be downloaded from the specified URL and resized to the specified dimensions before being pasted onto the image. If the object is text, it will be drawn onto the image using the specified font, size, and color. Finally