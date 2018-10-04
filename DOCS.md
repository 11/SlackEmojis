### Different flags and their meanings

1. `--workspace` or `-w`:
    - The subdomain used when logging into slack; often the name of the slack.
    - Example: company.slack.com
    - ie. <subdomain>.slack.com

2. `--email` or `-e`:
    - The email used to log into slack

3. `--password` or `-p`:
    - The password used to log into slack

4. `--url` or `-u`:
    - The url to an emoji you want uploaded

5. `--directory` or `-d`:
    - A relative path to a directory of emojis or images
    - When linking to a directory, this flag will search for *.gif, *.jpg, and *.png files and ignore all other filetypes


Example Command:
    slackmoji --workspace slack-name --email user@gmail.com --password abc123 --directory ./emojis/
    slackmoji -w slack-name -e user@gmail.com -p abc123 -d ./emojis/

    Either command is the same

Return a dictionary that contains the separate flags mapped to their values
