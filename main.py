import praw
import time

arr_comments = []
subreddit = "wallstreetbets"

reddit = praw.Reddit(client_id="qqV8kmfjpDEE9w",
                     client_secret="e6iVDV92IM7LyQRA1TOdPbYbT4w",
                     user_agent="wsbcommentscraper"
                     )
discussionPost = reddit.subreddit(subreddit).hot(limit=1)

def scrape_comments(state):
    if state == "y" or state == "Y":
        for post in discussionPost:
            print("Running, Please Be Patient.")
            post.comments.replace_more(limit=1)
            for comment in post.comments:
                try:
                    arr_comments.append(comment.body)
                except AttributeError:
                    pass
    print("Successfully Scraped The Comments")

def printComments(start):
    if start == 'Y'or start == "y":
        for comment in arr_comments:
            time.sleep(0.1)
            print(comment)

print("Welcome to the r/wsb Pinned Post Comment Scraper!")
time.sleep(2)
print("Booting Up")
time.sleep(1)
print("Accessing Subreddit")
time.sleep(3)
startScraping = str(input("Do you want to start scraping? Y/N: "))
scrape_comments(startScraping)
time.sleep(3)
print("You have scraped " + str(len(arr_comments)) + " comments")
time.sleep(2)
print("Do you want to print the comments?")
choice = str(input("Y/N; "))
time.sleep(2)
printComments(choice)
