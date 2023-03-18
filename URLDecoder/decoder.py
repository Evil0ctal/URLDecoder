#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author: https://github.com/Evil0ctal/
# @Time: 2023/03/17

import json
import urllib.parse
from typing import Union


class URLDecoder:

    @staticmethod
    def to_dict(encoded_url: str) -> dict:
        """
        Decode the URL-encoded string and convert it to a dictionary object
        """
        decoded_url = urllib.parse.unquote(encoded_url)
        parsed_url = urllib.parse.parse_qs(decoded_url)
        result = {}

        for key, value in parsed_url.items():
            try:
                result[key] = json.loads(value[0])
            except json.JSONDecodeError:
                result[key] = value[0]
        return result

    def to_json(self, encoded_url: str, indent=2, ensure_ascii=False) -> json:
        """
        Decode the URL-encoded string and convert it to a JSON object
        """
        decoded_json = self.to_dict(encoded_url)
        return json.dumps(decoded_json, indent=indent, ensure_ascii=ensure_ascii)

    @staticmethod
    def to_url(data: Union[dict, str]) -> str:
        """
        Convert the dictionary object or JSON object to a URL-encoded string
        """
        if isinstance(data, str):
            data = json.loads(data)
        return '&'.join(f"{urllib.parse.quote(key)}={urllib.parse.quote(str(value))}" for key, value in data.items())


if __name__ == "__main__":
    # Example URL-encoded string
    url_encoded_string = "name%3DAdam%20Tan%26age%3D99%26city%3DSan%20Jose%26cat_name%3DBurger%26hobbies%3D%7B%22most_do%22%3A%20%22programming%22%2C%20%22less_do%22%3A%20%22play_skateboard%22%2C%20%22others%22%3A%20%5B%22pool%22%2C%20%22pogo%22%2C%20%22airsoft%22%5D%7D%26job%3Dengineer"
    decoder = URLDecoder()

    dict_object = decoder.to_dict(url_encoded_string)
    print(dict_object)

    json_object = decoder.to_json(url_encoded_string)
    print(json_object)

    encoded_url = URLDecoder.to_url(json_object)
    print(encoded_url)
