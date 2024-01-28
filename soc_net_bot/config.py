import configparser
import sys


class ConfigHandler:
    def __init__(self, config_file="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_option(self, section: str, key: str, default: str) -> str:
        """Returns config option from default section in string representation.

        Args:
            section (str): The section in the configuration.
            key (str): The key by which you want to get the value from the configuration.
            default (str): Default value when it was not possible to get the value from the configuration.

        Returns:
            str: Value from configuration or default value.
        """
        try:
            option = self.config.get(section, key)
        except configparser.NoOptionError as err:
            print(err)
            print("Please double-check your config file")
            sys.exit(2)
        except configparser.NoSectionError as err:
            print(err)
            print("Please double-check your config file")
            sys.exit(2)
        if not option:
            return default
        return option
