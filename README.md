# TwitterBot_Height
There's a twitterbot made in Python which upload a tweet once a day with the name of a famous person and her/his height (in foots and meters)

**REMEMBER:** You'll need an account with permissions on API Development Kit of Twitter. 

You can ask for a developer account in [their website](http://developer.twitter.com/)

Last full test on ![](https://img.shields.io/badge/python-3.7-blue)

## Dependencies
`pip install tweepy` → Library to upload tweets

`pip install requests` → Library to download the picture using http

## Preview
This script will tweet this! 👇

![](https://github.com/fcoterroba/TwitterBot_Height/blob/main/tweet_preview.png)

## Automate
This script will tweet every time you run it.

But, that wouldn't really be a bot because depends of a human. Not cool.

I deployed the script over a VPS on Debian 10 and make a cronjob to run the script every day at 6 pm.

`00 18 * * * cd /path/to/the/where/are/the/script && /usr/bin/python3 main.py`

You can read more about crontab on [this website](https://crontab.guru/)

### License
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-red.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

You can read how I did this project on my website [Spanish](https://www.fcoterroba.com)
