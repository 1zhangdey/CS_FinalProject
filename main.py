import praw

reddit = praw.Reddit(client_id="qqV8kmfjpDEE9w",
                     client_secret="e6iVDV92IM7LyQRA1TOdPbYbT4w",
                     user_agent="wsbcommentscraper"
                     )

arr_comments = []

hot_posts = reddit.subreddit('wallstreetbets').hot(limit=1)
for post in hot_posts:
    for comment in post.comments:
        arr_comments.append(comment)

print(arr_comments)