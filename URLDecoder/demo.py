# pip install urldecoder
from URLDecoder.decoder import URLDecoder

# Example URL-encoded string
# url_encoded_string = input("Enter the URL-encoded string:")
url_encoded_string = "name%3DAdam%20Tan%26age%3D99%26city%3DSan%20Jose%26cat_name%3DBurger%26hobbies%3D%7B%22most_do%22%3A%20%22programming%22%2C%20%22less_do%22%3A%20%22play_skateboard%22%2C%20%22others%22%3A%20%5B%22pool%22%2C%20%22pogo%22%2C%20%22airsoft%22%5D%7D%26job%3Dengineer"

# Initialize the URLDecoder class
decoder = URLDecoder()

# Decode the URL-encoded string and convert it to a dictionary object
dict_object = decoder.to_dict(url_encoded_string)
print('dict_object:', dict_object)

# Convert the dictionary object to a JSON object
json_object = decoder.to_json(url_encoded_string)
print(json_object)

# Convert the JSON object to a URL-encoded string
encoded_url = URLDecoder.to_url(json_object)
print('encoded_url:', encoded_url)
