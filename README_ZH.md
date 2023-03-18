# URLDecoder

[English](./README.md) | [简体中文](./README_ZH.md)

## 介绍

URLDecoder 是一个简单而有效的 Python 库，旨在解码 URL 编码的字符串并将它们转换为 JSON 对象。该工具旨在简化将复杂的 URL 编码字符串转换为更易于阅读和管理的格式的过程。凭借其易于使用的功能，URLDecoder 可以成为任何需要处理和理解 URL 编码数据的项目的宝贵补充。无论您是处理 API、网络抓取还是数据分析任务，URLDecoder 都可以帮助您以结构化的方式高效地解码和解释 URL 参数。

## 安装

可以使用 pip 安装 URLDecoder:

```bash
pip install urldecoder
```

## 用法

URLDecoder 可用于解码 URL 编码的字符串并将其转换为 JSON 对象。以下示例演示如何使用 URLDecoder 解码 URL 编码的字符串：

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

上述代码的输出是:

```dict
dict_object: {'name': 'Adam Tan', 'age': 25, 'city': 'San Jose', 'cat_name': 'Burger', 'hobbies': {'most_do': 'programming', 'less_do': 'play_skateboard', 'others': ['pool', 'pogo', 'airsoft']}, 'job': 'engineer'}
```

```json
{
  "name": "Adam Tan",
  "age": 99,
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

## 贡献

欢迎请求请求。对于重大更改，请先打开一个问题来讨论您想要更改的内容。

请确保适当地更新测试。

## License

URLDecoder 根据 MIT 许可证获得许可。有关详细信息，请参阅 [LICENSE](LICENSE)
