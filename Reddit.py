# Author: Jorge Cisneros

# Reddit grabs users front page and prints it to the command line
# User can then choose an article to read and open the default browser
# on the users device.

# import modules
import subprocess
import sys
import webbrowser
import redditCreds as c

# import praw. If praw not installed, install praw and import
try:
    import praw
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "praw"])
finally:
    import praw

class Article:
    def __init__(self):
        self.title = ''
        self.sub = ''
        self.url = ''

# The reddit instance
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
        
        count = 1
        print()
        for i in self.ARTICLES:
            article = f"{count}) {i.title}\n"
            print(article)
            count += 1
        print()

if __name__ == "__main__":
    r = Reddit()
    r.GetReddit()
    
    selection = 0 

    while selection != 'q':
        selection = input("Print article (#) or (q)uit?: ")
        if selection != 'q':
            webbrowser.open(r.ARTICLES[int(selection)-1].url)

