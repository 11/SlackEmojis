### Different flags and their meanings

1. `--workspace` or `-w`: The subdomain used when logging into slack (the part that comes before `slack.com`)
    - ie. `<subdomain>.slack.com`

2. `--email` or `-e`: The email used to log into slack

3. `--password` or `-p`: The password used to log into slack

4. `--url` or `-u`: The url to an emoji you want uploaded

5. `--directory` or `-d`: A relative path to a directory of emojis or images
    - When linking to a directory, this flag will search for `*.gif`, `*.jpg`, and `*.png` files and ignore all other file types


### Run slackmoji Command
<b>Default Command</b>
``` 
slackmoji --workspace slack-name --email user@gmail.com --password abc123 --directory ./emojis/
```

<b>Abreviated Command</b>
``` 
slackmoji -w slack-name -e user@gmail.com -p abc123 -d ./emojis/
```
