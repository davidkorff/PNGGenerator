import json
import argparse
import urllib.parse

# Parse the command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("url", type=str, help="The URL with the JSON object")
args = parser.parse_args()

# Extract the JSON object from the URL
url_parts = urllib.parse.urlparse(args.url)
query_str = url_parts.query
query_dict = urllib.parse.parse_qs(query_str)
json_str = query_dict['template'][0]

# Convert the JSON string into a dictionary object
data = json.loads(json_str)

# Save the dictionary object to a file
with open('Art.json', 'w') as f:
    json.dump(data, f)
