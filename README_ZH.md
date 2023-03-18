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
from URLDecoder.decoder import URLDecoder

# 需要解码的 URL 编码字符串
url_encoded_string = "name=Adam%20Tan&age=25&city=San%20Jose"

# 初始化 URLDecoder 类
decoder = URLDecoder()

# 解码 URL 编码的字符串并将其转换为字典对象
decoded_url = decoder.to_dict(url_encoded_string)
print(decoded_url)

# 将字典对象转换为 JSON 对象
json_object = decoder.to_json(url_encoded_string)
print(json_object)
```

上述代码的输出是:

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

## 贡献

欢迎请求请求。对于重大更改，请先打开一个问题来讨论您想要更改的内容。

请确保适当地更新测试。

## License

URLDecoder 根据 MIT 许可证获得许可。有关详细信息，请参阅 [LICENSE](LICENSE)
