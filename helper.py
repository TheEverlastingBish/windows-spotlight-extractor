import os
import shutil
from PIL import Image


def get_files_list(loc):
    contents = [os.path.join(loc, f) for f in os.listdir(loc)]
    return contents


def rename_files(files_list):
    renamed_files = [f + '.jpg' for f in files_list]
    return renamed_files


def rename_file(file):
    renamed_file = file + '.jpg'
    return renamed_file


def compare_files(source_loc, target_loc):
    new_files = [f for f in get_files_list(source_loc) if rename_file(f) not in get_files_list(target_loc)]

    return new_files


def check_files(filename):
    pass


def check_image_dims(filename):
    try:
        im = Image.open(filename)
        if im.size in [(1920, 1080), (1080, 1920)]:
            return True
        else:
            return False
    except Image.UnidentifiedImageError:
        pass


def copy_files(source_file, target_file, metadata=False):
    if os.path.exists(source_file):
        if not os.path.exists(target_file):
            if metadata is True:
                shutil.copy2(source_file, target_file)
            else:
                shutil.copyfile(source_file, target_file)
        else:
            print("Target file exists!")
            pass
    else:
        print("Source path is invalid!")

