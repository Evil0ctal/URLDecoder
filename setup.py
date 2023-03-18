from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name="URLDecoder",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[],
    author="Evil0ctal",
    author_email="evil0ctal1985@gmail.com",
    description="A simple URL decoder that converts URL-encoded strings to JSON objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="encoded url decoder json",
    url="https://github.com/Evil0ctal/URLDecoder",
)
