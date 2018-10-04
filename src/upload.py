# Author: Doug Rudolph -- github.com/11
# Created: Sep 27th, 2018

import sys


def parse_cmd(cmd):
    mapped_cmd_params = {}
    flags = {
        '--workspace': 'workspace', '--email': 'email', '--password': 'password', '--url': 'url', '--directory': 'directory',
        '-w': 'workspace', '-e': 'email', '-p': 'password', '-u': 'url', '-d': 'directory'
    }

    for index,val in enumerate(cmd):
        if flags.get(val) is not None:
            try:
                mapped_cmd_params.update({flags[val]: cmd[index+1]})
            except Exception as err:
                raise err
        else:
            print(f'Parameter: {val} not recognized')
            sys.exit(0)

    return params


class Slack:
    """
    Object that keeps track of the slack session
    """

    def __init__(self, parsed_cmd)

        # One of the following parameters MUST NOT BE NONE
        self.url = self.parsed_cmd.get('url', None)
        self.directory = self.parsed_cmd.get('directory', None)

        if self.url is None and self.directory is None:
            print('command provided no url or directory')
            sys.exit(0)

        # Mandatory parameters
        self.email = self.parsed_cmd.get('email', None)
        self.password = self.parsed_cmd.get('password', None)
        self.workspace = self.parsed_cmd.get('workspace', None)

        if self.email is None or self.password is None or self.workspace is None:
            print('email, password, and workspace must be provided')
            sys.exit(0)

    def upload(self):
        pass

    def _upload_url(self):
        pass

    def _upload_dir(self):
        pass


if __name__ == '__main__':
    cmd = sys.argv
    parsed_cmd = parse_cmd(cmd)

    slack = Slack(parsed_cmd)
    slack.upload()


