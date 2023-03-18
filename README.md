# URLDecoder

[English](./README.md) | [简体中文](./README_ZH.md)

## Introduction

URLDecoder is a simple yet effective Python library designed to decode URL-encoded strings and convert them into JSON objects. This tool aims to streamline the process of transforming complex URL-encoded strings into a more human-readable and manageable format. With its easy-to-use functionality, URLDecoder can be a valuable addition to any project that requires processing and understanding URL-encoded data. Whether you are working with APIs, web scraping, or data analysis tasks, URLDecoder can help you efficiently decode and interpret URL parameters in a structured way.

## Installation

URLDecoder can be installed using pip:

```bash
pip install urldecoder
```

## Usage

URLDecoder can be used to decode URL-encoded strings and convert them into JSON objects. The following example demonstrates how to use URLDecoder to decode a URL-encoded string:

```python
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
```

The output of the above code is:

```dict
dict_object: {'name': 'Adam Tan', 'age': 25, 'city': 'San Jose', 'cat_name': 'Burger', 'hobbies': {'most_do': 'programming', 'less_do': 'play_skateboard', 'others': ['pool', 'pogo', 'airsoft']}, 'job': 'engineer'}
```

```json
{
  "name": "Adam Tan",
  "age": 25,
  "city": "San Jose",
  "cat_name": "Burger",
  "hobbies": {
    "most_do": "programming",
    "less_do": "play_skateboard",
    "others": [
      "pool",
      "pogo",
      "airsoft"
    ]
  },
  "job": "engineer"
}
```

```url
encoded_url: name=Adam%20Tan&age=25&city=San%20Jose&cat_name=Burger&hobbies=%7B%27most_do%27%3A%20%27programming%27%2C%20%27less_do%27%3A%20%27play_skateboard%27%2C%20%27others%27%3A%20%5B%27pool%27%2C%20%27pogo%27%2C%20%27airsoft%27%5D%7D&job=engineer
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

URLDecoder is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
