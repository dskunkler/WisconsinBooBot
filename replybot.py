#!/usr/bin/python
import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
        
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('uofmn')
for submission in subreddit.hot(limit=20):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("wisconsin", submission.selftext, re.IGNORECASE) or re.search("wisconsin", submission.title, re.IGNORECASE) :
            # Reply to the post
            submission.reply("Wisconsin?! BOOOOO")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)
        elif re.search("Badgers", submission.selftext, re.IGNORECASE) or re.search("badgers", submission.title, re.IGNORECASE) :
            # Reply to the post
            submission.reply("Badgers?! Wisconsin?! BOOOOO!")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)
            
        #limit more opens
        submission.comments.replace_more(limit = 1)
        
        #iterate through comments
        for c in submission.comments:
            
            #if comment not replied to already
            if c.id not in comments_replied_to:
                if re.search("badger", c.body, re.IGNORECASE) or re.search("badgers", c.body, re.IGNORECASE):
                    if c.author.name != "WisconsinBooBot":
                        c.reply("Badgers?! Wisconsin?! BOOOOO!")
                        comments_replied_to.append(c.id)
                        print("Bot replying to :", c.body, "\nauthor =", c.author.name)
                    
                elif re.search("wisconsin", c.body, re.IGNORECASE):
                    if c.author.name != "WisconsinBooBot":
                        c.reply("Wisconsin?! BOOOOO!")
                        comments_replied_to.append(c.id)
                        print("Bot replying to :", c.body, "\nauthor =", c.author.name)
            
    #if replied to still check comments
    elif submission.id in posts_replied_to:
        
        
        #limit more opens
        submission.comments.replace_more(limit = 1)
        
        #iterate through comments
        for c in submission.comments:
            
            #if comment not replied to already
            if c.id not in comments_replied_to:
                if re.search("badger", c.body, re.IGNORECASE) or re.search("badgers", c.body, re.IGNORECASE):
                    if c.author.name != "WisconsinBooBot":
                        c.reply("Badgers?! Wisconsin?! BOOOOO!")
                        comments_replied_to.append(c.id)
                        print("Bot replying to :", c.body, "\nauthor =", c.author.name)
                    
                elif re.search("wisconsin", c.body, re.IGNORECASE):
                    if c.author.name != "WisconsinBooBot":
                        c.reply("Wisconsin?! BOOOOO!")
                        comments_replied_to.append(c.id)
                        print("Bot replying to :", c.body,"\nAuthor =", c.author.name)
                    
        

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
        
with open("comments_replied_to.txt", "w") as g:
    for comment_id in comments_replied_to:
        g.write(comment_id + "\n")