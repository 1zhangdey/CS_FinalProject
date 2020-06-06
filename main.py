import praw

reddit = praw.Reddit(client_id="qqV8kmfjpDEE9w",
                     client_secret="e6iVDV92IM7LyQRA1TOdPbYbT4w",
                     user_agent="wsbcommentscraper")


hot_posts = reddit.subreddit("wallstreetbets").hot(limit=10)
for post in hot_posts:
    print(post.title)

