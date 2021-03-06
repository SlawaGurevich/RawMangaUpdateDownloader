from configparser import ConfigParser
import os

class ConfigHandler:
    def __init__(self, path_to_cfg=os.path.join(os.path.expanduser('~'), '.rawmangadownlaoder', 'conf.ini')):
        self.config = ConfigParser()
        self.path_to_cfg = path_to_cfg

        if not os.path.isfile(self.path_to_cfg):
            if not os.path.isdir(os.path.dirname(self.path_to_cfg)):
                try:
                    os.makedirs(os.path.dirname(self.path_to_cfg))
                except OSError as e:
                    print(e)

            if not os.path.isfile(self.path_to_cfg):
                try:
                    open(self.path_to_cfg, "w+").close()
                except OSError as e:
                    print(e)

        self.config.read(self.path_to_cfg)

    def set(self, section, option, value):
        self.config.set(section, option, value)
        self.save()

    def get(self, section, option, fallback=None):
        return self.config.get(section, option, fallback=fallback)

    def getboolean(self, section, option, fallback=None):
        return self.config.getboolean(section, option, fallback=fallback)

    def has_section(self, section):
        return self.config.has_section(section)

    def has_option(self, section, option):
        return self.config.has_option(section, option)

    def add_section(self, section):
        self.config.add_section(section)

    def save(self):
        with open(self.path_to_cfg, 'w+') as f:
            self.config.write(f)

    def load(self):
        self.config.read(self.path_to_cfg)