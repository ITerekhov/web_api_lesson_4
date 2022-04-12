from pathlib import Path

import requests

from additional_functions import download_image, get_file_extension


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


def main():
    # fetch_spacex_launch_by_id()
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
