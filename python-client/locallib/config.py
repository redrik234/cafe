import configparser
import os.path

class Config:
    CONFIG_PATH = os.path.dirname(__file__) + '/config/config.cfg'

    WEB_SECTION = 'web-config'
    WAV_SECTION = 'wav-config'
    DIR_SECTION = 'dir-config'

    __address = "localhost"
    __port  = 8081
    __wavConfig = []
    __wavDir = ""


    def __init__(self):
        if os.path.isfile(self.CONFIG_PATH) == False:
            raise ValueError('Config file not exist! Please create a config file: "%s"' % self.CONFIG_PATH)

        config = configparser.ConfigParser()
        config.read(self.CONFIG_PATH)
        
        self.__address = config.get(self.WEB_SECTION, 'address')
        self.__port = config.get(self.WEB_SECTION, 'port')

        self.__wavConfig = config[self.WAV_SECTION]

        self.__wavDir = config.get(self.DIR_SECTION, 'wavDir')
        if os.path.isdir(self.__wavDir) == False:
            raise ValueError('Directory (%s) does not exist. Check the config file!' % self.__wavDir)


    def getPort(self):
        return self.__port


    def getAddress(self):
        return self.__address


    def getWavConfig(self):
        return self.__wavConfig


    def getWavConfigProperty(self, property):
        if (property in self.__wavConfig) == False:
            raise ValueError('Property "%s" does not exist in a config. Check the config file!' % property)

        return self.__wavConfig[property]


    def getWavDir(self):
        return self.__wavDir