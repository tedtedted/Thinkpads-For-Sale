import re

from craigslist import CraigslistForSale
import praw

import settings

def craigslist_thinkpads():

    cl = CraigslistForSale(filters={'query':'T480'})

    for result in cl.get_results(sort_by='newest'):
        if 'T480' in result['name']:
            print(result)


def r_thinkpads():

    regex = '\[H\]*(?:(?!\[W\]).)*'

    reddit = praw.Reddit(client_id=settings.REDDIT_CLIENT_ID,
                     client_secret=settings.REDDIT_CLIENT_SECRET,
                     password=settings.REDDIT_PASSWORD,
                     user_agent=settings.REDDIT_USER_AGENT,
                     username=settings.REDDIT_USERNAME)

    subreddit = reddit.subreddit('thinkpadsforsale')

    for post in subreddit.new():
        if re.match(regex, 'T480') in post.title:
            print(post.title)

r_thinkpads()