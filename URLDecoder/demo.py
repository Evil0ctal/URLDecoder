from URLDecoder.decoder import URLDecoder


# Example URL-encoded string
url_encoded_string = "name=Adam%20Tan&age=25&city=San%20Jose"

# Initialize the URLDecoder class
decoder = URLDecoder()

# Decode the URL-encoded string and convert it to a dictionary object
decoded_url = decoder.to_dict(url_encoded_string)
print(decoded_url)

# Convert the dictionary object to a JSON object
json_object = decoder.to_json(url_encoded_string)
print(json_object)
