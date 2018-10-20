import praw

reddit = praw.Reddit(client_id='jW52Y1LgB9macg',
                     client_secret='1AXsqJzF3__OS-MMmKK5bv7iO8g',
                     user_agent='bobispro4')
print(reddit.read_only)

for submission in reddit.subreddit('wallstreetbets').new(limit=5):
    print(submission.title)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if(comment.author!="WSBVoteBot" and comment.author!="auto_moderator"):
            print(comment.body)