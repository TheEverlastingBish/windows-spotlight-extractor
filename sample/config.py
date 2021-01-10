# config.py

from configparser import ConfigParser
import json
import os


class AppConfig:
    """Interact with configuration variables."""

    configParser = ConfigParser()

    def __init__(self):
        self.repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.template_dir = (os.path.join(self.repo_dir, 'templates'))
        self.data_dir = (os.path.join(self.repo_dir, 'data'))
        self.log_dir = (os.path.join(self.repo_dir, 'log'))
        self.config_dir = os.path.join(self.repo_dir, "config")

        with open(os.path.join(self.config_dir, "config.json")) as cfg_file:
            self.cfg = json.load(cfg_file)

    @classmethod
    def setup_dirs(cls, template_dir, data_dir, log_dir):
        if not os.path.exists(template_dir):
            os.mkdir(template_dir)

        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
