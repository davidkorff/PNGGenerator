# extractor.py

This script extracts a JSON object from a URL and saves it to a file named Art.json.

To use this script, you will need to provide the URL as a command-line argument. For example:

```
python extractor.py "https://example.com?template={'key':'value'}"

python extractor.py https://davidkorff.github.io/SVGGenerator/?template={%20%22Template%22:%20{%20%22MaxTemplate%22:%20{%20%22Width%22:%20%22232.92%22,%20%22Height%22:%20%22251.92%22%20},%20%22PersonalizedObjects%22:%20[%20{%20%22PersonalizedObject%22:%20{%20%22ObjectType%22:%20%22IMG%22,%20%22ObjectContent%22:%20{%20%22imageURL%22:%20%22https://assets.pcna.com/image/upload/v1672267558/POD/MicrosoftTeams-image%20(38).png%22%20},%20%22ObjectLocation%22:%20{%20%22ObjectWidth%22:%20%22232.92%22,%20%22ObjectHeight%22:%20%22101%22,%20%22ObjectXOffset%22:%20%220%22,%20%22ObjectYOffset%22:%20%2260%22%20}%20}%20},%20{%20%22PersonalizedObject%22:%20{%20%22ObjectType%22:%20%22Text%22,%20%22ObjectContent%22:%20{%20%22Text%22:%20%22%22,%20%22FontSize%22:%20%2236%22,%20%22FontColor%22:%20%22000000%22%20},%20%22ObjectLocation%22:%20{%20%22ObjectWidth%22:%20%22232.92%22,%20%22ObjectHeight%22:%20%22101%22,%20%22ObjectXOffset%22:%20%220%22,%20%22ObjectYOffset%22:%20%2260%22%20}%20}%20}%20]%20}%20}
```

The JSON object must be passed as the value of the template query parameter in the URL.

# create_png.py

This script reads a JSON object from a file named Art.json and generates a PNG image from it. The image will be saved to a file named Full_Template.png.

The JSON object is expected to contain a dictionary with the following structure:

```

  "Template": {
    "MaxTemplate": {
      "Width": "232.92",
      "Height": "251.92"
    },
    "MaxDecoArea": {
      "Width": "232.92",
      "Height": "101.6",
      "DecoXOffset": "0",
      "DecoYOffset": "60"
    },
    "PersonalizedObjects": [
      {
        "PersonalizedObject": {
          "ObjectType": "IMG",
          "ObjectContent": {
            "imageURL": "https://assets.pcna.com/image/upload/v1672351495/POD/L407182_4x4_DIP.png"
          },
          "ObjectLocation": {
            "ObjectWidth": "",
            "ObjectHeight": "",
            "ObjectXOffset": "25%",
            "ObjectYOffset": "50%"
          }
        }
      },
      {
        "PersonalizedObject": {
          "ObjectType": "Text",
          "ObjectContent": {
            "Text": "David",
            "FontSize": "40",
            "FontColor": "000000",
            "Font": "arial.ttf"
          },
          "ObjectLocation": {
            "ObjectWidth": "0",
            "ObjectHeight": "0",
            "ObjectXOffset": "75%",
            "ObjectYOffset": "75%"
          }
        }
      }
    ]
  }
}

```

The `MaxDecoArea` object specifies the dimensions of the resulting image. The PersonalizedObjects list contains objects that will be added to the image. Each object can be either an image (specified with the `IMG` `ObjectType`) or text (specified with the `Text` `ObjectType`).

The `MaxTemplate` object specifies the dimensions of the resulting 'Full_Temaplate"". The `DecoArea.png` will be pasted on this the full template, using the offsets in the object.

The `ObjectContent` object for an image object should contain an `imageURL` field with the URL of the image to be added to the image.

The `ObjectContent` object for a text object should contain a `Text` field with the text to be added to the image, a `FontSize` field with the font size in pixels, and a `FontColor` field with the font color in hexadecimal format.

The `ObjectLocation` object specifies the dimensions and position of the object on the image. The `ObjectWidth` and `ObjectHeight` fields specify the dimensions of the object in pixels, and the `ObjectXOffset` and `ObjectYOffset` fields specify the distance from the top-left corner of the image to the top-left corner of the object.

The script will read the JSON object and create an image with a transparent background. It will then iterate over the `PersonalizedObjects` list and add each object to the image. If the object is an image, it will be downloaded from the specified URL and resized to the specified dimensions before being pasted onto the image. If the object is text, it will be drawn onto the image using the specified font, size, and color.


