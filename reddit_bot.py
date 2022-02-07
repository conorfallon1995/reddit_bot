import praw
import config
import time
import os
import requests
import querier


#UNIT TEST HERE
def bot_login():
    print("Logging in...")

    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="CF test of basic reddit bot v0.1")
    print("Logged in!")

    #print(r.user)
    return r


def run_bot(r, comments_replied_to):
    print("Obtaining 25 comments...")

    for comment in r.subreddit('test').comments(limit=25):
        if "!film" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("String with \"!film\" found in comments " + comment.id)

            comment_reply = "You have requested Mini-Movie-Recommender-Bot. Here's a bit of info: \n \n"
            print("Replied to comment " + comment.id)

            # Format strings
            sql_string = comment.body[6:len(comment.body)]
            #  .title() ensures that it will be correctly capitalised
            json_string = sql_string.replace(" ", "_").title()
            url_string = "https://en.wikipedia.org/api/rest_v1/page/summary/" + json_string

            # This has been modified to return a wikipedia extract WILL CRASH IF TRY EXCEPT NOT HERE
            # UNIT TEST GOES HERE

            film = ""

            try:
                film = requests.get(url_string).json()['extract']
            except KeyError:
                print('Blame the editors...')

            # Now add the bit from the querier.py file

            comment_reply += querier.string_query(sql_string)

            # Then the wiki bit

            comment_reply += "\nHere is a bit of info about that movie, kindly provided by our friends at Wikipedia:\n"
            comment_reply += ">" + film + "\n"

            comments_replied_to.append(comment.id)

            comment.reply(comment_reply)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print(comments_replied_to)
    print("Sleeping for ten seconds...")
    # Sleep for ten seconds
    time.sleep(10)

# Keeps a record of comments replied to so as to avoid spamming and getting exiled from Reddit...

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to



comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(bot_login(), comments_replied_to)
