import re

from craigslist import CraigslistForSale
import praw

import settings

MODEL = 'T480'


def main():
    print('Checking Craigslist')
    craigslist_thinkpads()

    print('Checking r/Thinkpadsforsale')
    r_thinkpads()


def craigslist_thinkpads():

    cl = CraigslistForSale(filters={'query':MODEL})

    for result in cl.get_results(sort_by='newest'):
        if MODEL in result['name']:
            print(result)


def r_thinkpads():

    regex = re.compile(rf'\[H\].*({MODEL}).* (.*?)\[W\]')

    reddit = praw.Reddit(client_id=settings.REDDIT_CLIENT_ID,
                     client_secret=settings.REDDIT_CLIENT_SECRET,
                     password=settings.REDDIT_PASSWORD,
                     user_agent=settings.REDDIT_USER_AGENT,
                     username=settings.REDDIT_USERNAME)

    subreddit = reddit.subreddit('thinkpadsforsale')

    for post in subreddit.new():
        if regex.search(post.title):
            print(post.title)


if __name__ == '__main__':
    main()