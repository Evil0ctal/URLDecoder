# URLDecoder

URLDecoder is a simple yet effective Python library designed to decode URL-encoded strings and convert them into JSON objects. This tool aims to streamline the process of transforming complex URL-encoded strings into a more human-readable and manageable format. With its easy-to-use functionality, URLDecoder can be a valuable addition to any project that requires processing and understanding URL-encoded data. Whether you are working with APIs, web scraping, or data analysis tasks, URLDecoder can help you efficiently decode and interpret URL parameters in a structured way.

## Installation

URLDecoder can be installed using pip:

```bash
pip install urldecoder
```

## Usage

URLDecoder can be used to decode URL-encoded strings and convert them into JSON objects. The following example demonstrates how to use URLDecoder to decode a URL-encoded string:

```python
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
```

The output of the above code is:

```dict
{'name': 'Adam Tan', 'age': 25, 'city': 'San Jose'}
```

```json
{
    "name": "Adam Tan",
    "age": "25",
    "city": "San Jose"
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

URLDecoder is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
