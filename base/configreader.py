"""
@package base

ConfigReader class implementation

It reads the configuration files needed for the framework

All the methods to read different configuration file should be implemented in Util class

Example:
    self.cfg = ConfigReader(fileName=fileName)
    self.cfg.configRead()
    value = self.cfg.getConfiguration(section, option)
"""
from configparser import ConfigParser
import os


class ConfigReader(object):
    def __init__(self, file_name="messages.ini"):
        self.parser = ConfigParser()
        script_directory = os.path.dirname(__file__)
        relative_path = "../configfiles/" + file_name
        abs_file_path = os.path.join(script_directory, relative_path)
        self.file = abs_file_path

    # self.file = ['/auto/home.nas03/atomar/hg/ntests/cases/gui/configfiles/testenvironment.ini']

    def config_read(self):
        self.parser.read(self.file)

    def config_section_map(self, section):
        """
        Returns a dictionary of 'Option and Value' under a section

        Required Parameters:
            section: Section in the file under which options exist
                     Look at messages.ini to understand the format of a configuration file

        Optional Parameters:
            None

        Returns:
            Dictionary of 'Option and Value'
        """
        config = {}
        options = self.parser.options(section)
        for option in options:
            try:
                config[option] = self.parser.get(section, option)
                if config[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                config[option] = None
        return config

    def get_configuration(self, section, option):
        """
        Get value of the provided option and section

        Required Parameters:
            section: Section in the file under which options exist
            option: Option whose corresponding value is needed

        Optional Parameters:
            None

        Returns:
            Value of the provided option
        """
        config_map = self.config_section_map(section)
        option_value = config_map[option]
        return option_value

    def test_method(self):
        value = ConfigReader.get_configuration(self, 'Grid', 'remote')
        print(value)
