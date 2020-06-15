import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id="qqV8kmfjpDEE9w",
                     client_secret="e6iVDV92IM7LyQRA1TOdPbYbT4w",
                     user_agent="wsbcommentscraper"
                     )

arr_comments = []

discussionPost = reddit.subreddit('wallstreetbets').hot(limit=1)


for post in discussionPost:
    post.comments.replace_more(limit=3)
    for comment in post.comments:
        try:
            arr_comments.append(comment.body )
        except AttributeError:
            pass

print(arr_comments)