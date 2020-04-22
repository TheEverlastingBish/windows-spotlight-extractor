import os

SOURCE_LOC = r"~\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"


class AppConfig:

    repo_dir = os.path.dirname(os.path.abspath(__file__))
    print(repo_dir)

    template_dir = (os.path.join(repo_dir, 'templates'))
    print(template_dir)

    data_dir = (os.path.join(repo_dir, 'data'))
    print(data_dir)

    log_dir = (os.path.join(repo_dir, 'log'))
    print(log_dir)

    @classmethod
    def setup_dirs(cls, template_dir=template_dir, data_dir=data_dir, log_dir=log_dir):
        if not os.path.exists(template_dir):
            os.mkdir(template_dir)

        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
