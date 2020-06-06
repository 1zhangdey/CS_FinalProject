import praw

reddit = praw.Reddit(client_id="qqV8kmfjpDEE9w",
                     client_secret="e6iVDV92IM7LyQRA1TOdPbYbT4w",
                     user_agent="wsbcommentscraper"
                     )
sub = reddit.submission("wallstreetbets")
pinnedPost = sub.hot(limit =1)
arr_comment = []
counter = 500

for post in pinnedPost:
    post.comments.replace_more(limit=0)
    for comment in post.comments.list():
        arr_comment.append(comment)




print(arr_comment)

