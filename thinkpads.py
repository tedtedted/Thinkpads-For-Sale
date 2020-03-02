import os
import re

from dotenv import load_dotenv

load_dotenv()

from craigslist import CraigslistForSale
import praw

MODEL = "T480"

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")


def main():
    print("Checking Craigslist")
    craigslist_thinkpads()

    print("Checking r/Thinkpadsforsale")
    r_thinkpads()


def craigslist_thinkpads():

    cl = CraigslistForSale(filters={"query": MODEL})

    for result in cl.get_results(sort_by="newest"):
        if MODEL in result["name"]:
            print(result)


def r_thinkpads():

    regex = re.compile(rf"\[H\].*({MODEL}).* (.*?)\[W\]")

    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        password=REDDIT_PASSWORD,
        user_agent=REDDIT_USER_AGENT,
        username=REDDIT_USERNAME,
    )

    subreddit = reddit.subreddit("thinkpadsforsale")

    for post in subreddit.new():
        if regex.search(post.title):
            print(post.title)


if __name__ == "__main__":
    main()
