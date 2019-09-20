#!/usr/bin/python3
" queries the Reddit API "
from requests import get


def number_of_subscribers(subreddit):
    " Returns the number of subscribers "
    header = {'User-Agent': 'My User Agent 1.0'}
    try:
        api_reddit = "https://www.reddit.com"
        link_url = get('{}/r/{}/about.json'.format(api_reddit, subreddit),
                       headers=header, allow_redirects=False).json()
        return link_url.get('data').get('subscribers')
    except:
        return 0
