# Utils
import os
import json

# Project Packages
from config import AppConfig
import helper


def main():

    app_config = AppConfig()
    app_config.setup_dirs(app_config.template_dir, app_config.data_dir, app_config.log_dir)

    # print(json.dumps(app_config.cfg, indent=4))

    source_loc = os.path.expanduser(app_config.cfg.get("ws_location"))
    print("Windows Spotlight Source Location:", source_loc)

    target_loc = os.path.expanduser(app_config.cfg.get("target_location"))
    print("Target Location:", target_loc)

    source_files = helper.get_files_list(source_loc)
    print("Total {} files found in source location.".format(len(source_files)))

    device_properties = app_config.cfg.get("device_properties")
    valid_dims = [(v.get("image_width"), v.get("image_height")) for k, v in device_properties.items()]
    print("List of valid dimensions:", valid_dims)

    valid_source_set = helper.get_valid_images(source_files, valid_dims)  # List[Tuple[str, str]]
    print("Valid source files:", len(valid_source_set))

    valid_source_files = []
    target_files = []

    for img_file, img_type in valid_source_set:
        valid_source_files.append(img_file)

        target_file = os.path.join(target_loc, img_type,
                                   helper.add_file_extension(os.path.basename(img_file), ext='.jpg'))
        target_files.append(target_file)

    valid_file_set = helper.get_valid_target_files(valid_source_files, target_files)  # List[Tuple[str, str]]
    print("Files to extract:", len(valid_file_set))

    if len(valid_file_set) > 0:
        helper.transfer_files(valid_file_set, mode='copy')
    else:
        print("No new files to transfer!")


if __name__ == '__main__':
    main()
