import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def get_url():
        url = config.get('comm', 'baseurl')
        return url

    @staticmethod
    def get_username():
        username = config.get('comm', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('comm', 'password')
        return password
