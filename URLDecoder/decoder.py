#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author: https://github.com/Evil0ctal/
# @Time: 2023/03/17

import json
import urllib.parse


class URLDecoder:

    @staticmethod
    def to_dict(encoded_url: str) -> dict:
        parsed_url = urllib.parse.parse_qs(encoded_url)
        result = {}

        for key, value in parsed_url.items():
            try:
                result[key] = json.loads(value[0])
            except json.JSONDecodeError:
                result[key] = value[0]
        return result

    def to_json(self, encoded_url: str, indent=2, ensure_ascii=False) -> json:
        decoded_json = self.to_dict(encoded_url)
        return json.dumps(decoded_json, indent=indent, ensure_ascii=ensure_ascii)


if __name__ == "__main__":
    url_encoded_string = "name=Adam%20Tan&age=25&city=San%20Jose"
    decoder = URLDecoder()
    decoded_url = decoder.to_dict(url_encoded_string)
    print(decoded_url)
    json_object = decoder.to_json(url_encoded_string)
    print(json_object)
