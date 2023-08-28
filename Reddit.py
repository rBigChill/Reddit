import subprocess
import sys

try:
    import praw
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "praw"])
finally:
    import praw

import redditCreds as c

class Article:
    def __init__(self):
        self.title = ''
        self.sub = ''
        self.url = ''

class Reddit:
    def __init__(self):
        self.REDDIT = praw.Reddit(
                client_id = c.CLIENT_ID,
                client_secret = c.CLIENT_SECRET,
                user_agent = c.USER_AGENT,
                username = c.USERNAME,
                password = c.PASSWORD,
                )
        self.ARTICLES = []

    def _grabArticles(self):

        for submission in self.REDDIT.front.hot(limit=10):
            a = Article()
            a.title = submission.title
            a.sub = submission.subreddit.display_name
            a.url = submission.url
            self.ARTICLES.append(a)
        
    def GetReddit(self):
        self._grabArticles()

        print()
        for i in self.ARTICLES:
            article = f"{i.title}\n"
            print(article)
        print()

if __name__ == "__main__":
    r = Reddit()
    r.GetReddit()
