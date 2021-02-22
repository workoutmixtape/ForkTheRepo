import os


class Conf:
    DEBUG = True


class TestConf(Conf):
    TESTING = True
    GITHUB_CLIENT_ID='testclientid'
    GITHUB_CLIENT_SECRET='testclientsecret'


class PrdConf(Conf):
    DEBUG = False
    GITHUB_CLIENT_ID=os.environ['GITHUB_CLIENT_ID']
    GITHUB_CLIENT_SECRET=os.environ['GITHUB_CLIENT_SECRET']
