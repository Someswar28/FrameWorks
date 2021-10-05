import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\hp\\pythonProject\\FrameWorks\\Configurations\\config.ini")


class read_config:

    @staticmethod
    def geturl():
        url = config.get('Common Info', 'BaseURL')
        return url

    @staticmethod
    def getusername():
        username = config.get('Common Info', 'Username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('Common Info', 'Password')
        return password
