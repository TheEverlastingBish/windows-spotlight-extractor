import os
import config
from config import AppConfig
import helper


def main():

    app_config = AppConfig
    app_config.setup_dirs()

    source_loc = os.path.expanduser(config.SOURCE_LOC)
    source_files = helper.get_files_list(source_loc)

    new_files = helper.compare_files(source_loc, app_config.data_dir)

    for f in new_files:
        target_file = os.path.join(app_config.data_dir, helper.rename_file(os.path.basename(f)))

        if helper.check_image_dims(f) is True:
            helper.copy_files(f, target_file)
            print(target_file)


if __name__ == '__main__':
    main()
