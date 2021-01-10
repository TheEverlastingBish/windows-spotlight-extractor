# Utils
import os
import shutil
import re
from datetime import datetime
from typing import Union, Any, List, Dict, Tuple

# Core
from PIL import Image

# Project
from config import AppConfig


app_config = AppConfig()


def assert_list(x: Any) -> List[Any]:
    """Checks if list and forces return as a list."""

    if isinstance(x, list):
        return x
    elif isinstance(x, str):
        return [y.strip() for y in x.split(sep=',')]
    elif isinstance(x, tuple):
        return list(x)
    else:
        return [x]  # int, float, etc.


def gen_timestamp(date_only=False, supplied_date=None, file_name=False):
    if date_only is True:
        format_string = '%Y-%m-%d'
    elif file_name is True:
        format_string = '%Y-%m-%d_%H-%M-%S'
    else:
        format_string = '%Y-%m-%d %H:%M:%S'

    if supplied_date:
        use_date = supplied_date
    else:
        use_date = datetime.today()

    load_date = use_date.strftime(format_string)
    return load_date


def get_files_list(locs):
    contents = []
    locs = assert_list(locs)

    for loc in locs:
        if os.path.exists(loc):
            files = [os.path.join(loc, f.name) for f in os.scandir(loc) if f.is_file()]
            contents.extend(files)
    return contents


def add_file_extension(file, ext='.jpg'):

    renamed_file = file + ext
    return renamed_file


def get_image_type(img_dim):
    """Check Image Dimensions and Return Image Type"""

    try:
        if img_dim == (1920, 1080):
            return 'Desktop'
        elif img_dim == (1080, 1920):
            return 'Mobile'
        else:
            return False
    except Image.UnidentifiedImageError:
        pass


def get_valid_images(file_list: List[str],
                     valid_dim_list: List[Tuple[int, int]]) -> List[Tuple[str, str]]:
    """Check Image Dimensions Match Requirements and Return Valid Images"""

    valid_files = []
    for fl in file_list:
        try:
            im = Image.open(fl)
            if im.size in valid_dim_list:
                valid_files.append((fl, get_image_type(im.size)))
        except Image.UnidentifiedImageError as uie:
            # print("Unidentified image:", uie)
            pass
    return valid_files


def get_valid_target_files(source_list: List[str],
                           target_list: List[str]) -> List[Tuple[str, str]]:

    valid_list = [(sfl, tfl) for sfl, tfl in zip(source_list, target_list) if not os.path.exists(tfl)]
    return valid_list


def get_destination(alpha_destination):
    if os.path.exists(alpha_destination):
        final_destination = alpha_destination
    else:
        final_destination = app_config.data_dir
        print("Destination '{}' not valid!\nSaving to '{}'".format(alpha_destination, final_destination))
    return final_destination


def transfer_files(file_pairs: List[Tuple[str, str]], mode: str = 'copy') -> None:
    """
    Copy or Move files within disk
    :param file_pairs: List of tuples containing source and target paths to copy/move.
    :param mode: A string, either 'copy' or 'move'. Default is 'copy'
    """

    for file_set in file_pairs:
        try:
            if os.path.exists(file_set[0]):
                if mode == 'move':
                    print("Moving: {}".format(file_set[1]))
                    shutil.move(file_set[0], file_set[1])
                else:
                    print("Copying: {}".format(file_set[1]))
                    shutil.copy(file_set[0], file_set[1])
            else:
                raise FileNotFoundError
        except Exception as e:
            print(e)

