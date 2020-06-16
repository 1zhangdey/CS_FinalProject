import praw
import time


arr_comments = []

reddit = praw.Reddit(client_id="qqV8kmfjpDEE9w",
                     client_secret="e6iVDV92IM7LyQRA1TOdPbYbT4w",
                     user_agent="wsbcommentscraper"
                     )
discussionPost = reddit.subreddit("wallstreetbets").hot(limit=1)

def scrape_comments(state):
    if state == True:
        for post in discussionPost:
            print("Running, Please Be Patient")
            post.comments.replace_more(limit=1)
            for comment in post.comments:
                try:
                    arr_comments.append(comment.body)
                except AttributeError:
                    pass
    print("Successfully Scraped The Comments")


#start of program
print("Welcome to the Reddit Comment Scraper!")
time.sleep(3)
print("Booting Up")
time.sleep(1)
subreddit = str(input("What Subreddit can I scrap for you today?"))
time.sleep(2)
print("Very nice choice sir")
time.sleep(1)
print("Accessing Subreddit")