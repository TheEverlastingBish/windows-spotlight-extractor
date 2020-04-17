import os
import shutil
from PIL import Image


def get_files_list(loc):
    contents = os.path.listdir(loc)

    return contents


def compare_files(source_loc, target_loc):
    new_files = [f for f in get_files_list(source_loc) if f not in get_files_list(target_loc)]

    return new_files


def rename_files(files_list):
    renamed_files = [f + '.jpg' for f in files_list]
    return renamed_files


def copy_files(source_file, target_file, metadata=False):
    if os.path.exists(source_file):
        if os.path.exists(target_file):
            if metadata is True:
                shutil.copy2(source_file, target_file)
            else:
                shutil.copyfile(source_file, target_file)
        else:
            print("Target path is invalid!")
    else:
        print("Source path is invalid!")

