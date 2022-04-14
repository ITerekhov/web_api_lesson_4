from urllib.parse import urlparse, unquote
from os.path import splitext

import requests


def download_image(image_url, download_path, params=None):
    response = requests.get(image_url, params=params)
    response.raise_for_status()
    with open(str(download_path), 'wb') as file:
        file.write(response.content)


def get_file_extension(url: str):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    return splitext(path)[1]