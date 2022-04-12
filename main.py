import datetime
import os
from os.path import splitext
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from dotenv import load_dotenv


def download_image(image_url, download_path, params=None):
    if params:
        response = requests.get(image_url, params=params)
    else:
        response = requests.get(image_url)
    response.raise_for_status()
    with open(str(download_path), 'wb') as file:
        file.write(response.content)


def get_file_extension(url: str):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    return splitext(path)[1]


def fetch_spacex_last_launch():
    images_dir = 'images/'
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    links_img = response.json()['links']['flickr']['original']
    for number_img, link_img in enumerate(links_img):
        img_extension = get_file_extension(link_img) 
        path_img = images_dir + 'spacex' + str(number_img + 1) + img_extension
        download_image(link_img, path_img)


def fetch_spacex_launch_by_id(id: str = '6234908cf051102e1fcedac4'):
    images_dir = 'images/'
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    links_img = response.json()['links']['flickr']['original']
    for number_img, link_img in enumerate(links_img):
        img_extension = get_file_extension(link_img) 
        path_img = images_dir + 'spacex' + str(number_img + 1) + img_extension
        download_image(link_img, path_img)


def fetch_astronomy_picture_from_nasa(count: int, nasa_request_params: dict):
    apod_images_dir = 'apod_images/'
    Path(apod_images_dir).mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    nasa_request_params['count'] = count
    response = requests.get(url, params=nasa_request_params)
    response.raise_for_status()
    links_img = [link['hdurl'] for link in response.json()]
    for number_img, link_img in enumerate(links_img):
        img_extension = get_file_extension(link_img)
        path_img = apod_images_dir + 'apod' + str(number_img + 1)
        path_img += img_extension
        download_image(link_img, path_img)


def fetch_EPIC_photo(count: int, nasa_request_params: dict):
    epic_images_dir = 'EPIC_images/'
    Path(epic_images_dir).mkdir(parents=True, exist_ok=True)
    get_json_url = 'https://epic.gsfc.nasa.gov/api/natural'
    get_photo_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    response = requests.get(get_json_url)
    response.raise_for_status()
    images = response.json()
    for index in range(count):
        date = datetime.datetime.fromisoformat(images[index]['date'])
        date = date.strftime("%Y/%m/%d")
        img_id = images[index]['image']
        link_img = get_photo_url + f'/{date}/png/{img_id}.png'
        img_extension = '.png'
        path_img = epic_images_dir + img_id + img_extension
        download_image(link_img, path_img, params=nasa_request_params)


def main():
    load_dotenv()
    nasa_api_token = os.getenv('NASA_API_TOKEN')
    nasa_request_params = {'api_key': nasa_api_token}
    fetch_spacex_launch_by_id()
    fetch_astronomy_picture_from_nasa(2, nasa_request_params)
    fetch_EPIC_photo(2, nasa_request_params)


if __name__ == '__main__':
    main()