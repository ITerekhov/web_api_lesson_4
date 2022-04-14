import argparse
from pathlib import Path

import requests

from additional_functions import download_image, get_file_extension

def fetch_spacex_launch(launch_id:str):
    images_dir = 'images/'
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    query_param = launch_id if launch_id else 'latest'
    url = f'https://api.spacexdata.com/v5/launches/{query_param}'
    response = requests.get(url)
    response.raise_for_status()
    links_img = response.json()['links']['flickr']['original']
    for number_img, link_img in enumerate(links_img, start=1):
        img_extension = get_file_extension(link_img)
        path_img = f'{images_dir}spacex{str(number_img)}{img_extension}'
        download_image(link_img, path_img)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--launch_id',
        type=str,
        default=None,)
    launch_id = parser.parse_args().launch_id
    fetch_spacex_launch(launch_id)


if __name__ == '__main__':
    main()
