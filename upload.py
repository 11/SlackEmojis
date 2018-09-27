import requests
import os


class Slack:

    def __init__(self, username, password, workspace):
        self.username = username
        self.password = password
        self.workspace = workspace

    def upload(self):
        pass


class Aggregator:

    def collect_local_emojis(self, filepath):
        pass

    def collect_emoji_by_url(self, url):
        pass


class Parser:
    pass


if __name__ == '__main__':
    pass
