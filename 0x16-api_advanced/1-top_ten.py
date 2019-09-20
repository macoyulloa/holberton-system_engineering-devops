#!/usr/bin/python3
" queries the Reddit API "
from requests import get


def top_ten(subreddit):
    " prints the 10 hot post listed "
    header = {'User-Agent': 'My User Agent 1.0'}
    try:
        api_reddit = "https://www.reddit.com"
        link_url = get('{}/r/{}/about.json?limit=10&sort=hot'
                       .format(api_reddit, subreddit),
                       headers=header, allow_redirects=False).json()
        data = link_url.get('data')
        for child in data.get('children'):
            print(child['data']['title'])
    except:
        print(None)
