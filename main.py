import praw
import tkinter as tk


window = tk.Tk()


label = tk.Label(text= "r/WSB Comment Scraper!!!", foreground = "white",background = "black",)
label.pack()

button = tk.Button(text = "Start Program", width = 40, height = 30, )
button.pack()


window.mainloop()







reddit = praw.Reddit(client_id="qqV8kmfjpDEE9w",
                     client_secret="e6iVDV92IM7LyQRA1TOdPbYbT4w",
                     user_agent="wsbcommentscraper"
                     )

arr_comments = []

discussionPost = reddit.subreddit('wallstreetbets').hot(limit=1)



def scrape_comments():
    for post in discussionPost:
        post.comments.replace_more(limit=4)
        for comment in post.comments:
            try:
                arr_comments.append(comment.body)
            except AttributeError:
                pass

