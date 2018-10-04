# Author: Doug Rudolph -- github.com/11
# Created: Sep 27th, 2018

import sys


class Slack:
    """
    Object that keeps track of the slack session
    """

    def __init__(self, parsed_cmd)

        # One of the following parameters MUST NOT BE NONE
        self.url = self.parsed_cmd.get('url', None)
        self.directory = self.parsed_cmd.get('directory', None)

        if url is None and directory is None:
            print('command provided no url or directory')
            sys.exit(0)

        # Mandatory parameters
        self.email = self.parsed_cmd['email']
        self.password = self.parsed_cmd['password']
        self.workspace = self.parsed_cmd['workspace']

    def upload(self):
        pass

    def _upload_url(self):
        pass

    def _upload_dir(self):
        pass


def parse_cmd(command):
    """
    Different flags and their meanings

    1.) --workspace or -w:
        - The subdomain used when logging into slack; often the name of the slack.
        - Example: company.slack.com
        - ie. <subdomain>.slack.com

    2.) --email or -e:
        - The email used to log into slack

    3.) --password or -p:
        - The password used to log into slack

    4.) --url or -u:
        - The url to an emoji you want uploaded

    5.) --directory or -d :
        - A relative path to a directory of emojis or images
        - When linking to a directory, this flag will search for *.gif, *.jpg, and *.png files and ignore all other filetypes


    Example Command:
        slackmoji --workspace slack-name --email user@gmail.com --password abc123 --directory ./emojis/
        slackmoji -w slack-name -e user@gmail.com -p abc123 -d ./emojis/

        Either command is the same

    Return a dictionary that contains the separate flags mapped to their values
    """
    params = {}
    flags = {
        '--workspace': 'workspace',
        '--email': 'email',
        '--password': 'password',
        '--url': 'url',
        '--directory': 'directory',
        '-w': 'workspace',
        '-e': 'email',
        '-p': 'password',
        '-u': 'url',
        '-d': 'directory'
    }

    for index,val in enumerate(command):
        if flags.get(val) is not None:
            try:
                params.update({flags[val]: command[index+1]})
            except Exception as err:
                raise err
        else:
            print(f'Parameter: {val} not recognized')
            sys.exit(0)

    return params

if __name__ == '__main__':
    cmd = sys.argv
    parsed_cmd = parse_cmd(cmd)

    slack = Slack(parsed_cmd)
    slack.upload()


