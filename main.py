import praw
reddit = praw.Reddit(client_id='jW52Y1LgB9macg',
                     client_secret='1AXsqJzF3__OS-MMmKK5bv7iO8g',
                     user_agent='bobispro4')
print(reddit.read_only)


def readSub(subreddit,sorter,number):
    global reddit
    all=[]
    sort = None
    sub = reddit.subreddit(subreddit)
    if (sorter == "hot"):
        sort = sub.hot(limit=number)
    if (sorter == "top"):
        sort = sub.top(limit=number)
    if (sorter == "new"):
        sort = sub.new(limit=number)
    for submission in sort:
    # submission.comments.replace_more(limit=None)
    # for comment in submission.comments.list():
    #     if(comment.author!="WSBVoteBot" and comment.author!="auto_moderator"):
    #         all+= comment.body
        submission.comments.replace_more(limit=None)
        all.append(submission.title)
        for top_level_comment in submission.comments:
            all.append(top_level_comment.body)
            for second_level_comment in top_level_comment.replies:
                all.append(second_level_comment.body)
                for third_level_comment in second_level_comment.replies:
                    all.append(third_level_comment.body)
    return all