import praw
import config
import time
import os
import requests
import main

def bot_login():
    print("Logging in...")

    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="CF test of basic reddit bot v0.1")
    print("Logged in!")

    return r


def run_bot(r, comments_replied_to):
    print("Obtaining 25 comments...")

    for comment in r.subreddit('test').comments(limit=25):
        if "!joke" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("String with \"!joke\" found in comments " + comment.id)

            comment_reply = "You requested a joke about Chuck Norris! Here it is: \n \n"
            print("Replied to comment " + comment.id)

            # Format strings
            sql_string = comment.body[6:len(comment.body)]
            #  .title() ensures that it will be correctly capitalised
            json_string = sql_string.replace(" ", "_").title()
            url_string = "https://en.wikipedia.org/api/rest_v1/page/summary/" + json_string

            # TO DO: Need to pass the sql string into the main, OR import the necessary functionality
            # from the main function; have a think about which will work best

            # This has been modified to return a wikipedia extract WILL CRASH IF TRY EXCEPT NOT HERE


            joke = ""

            try:
                joke = requests.get(url_string).json()['extract']
            except KeyError:
                print('Blame the editors...')

            comment_reply += ">" + joke

            comments_replied_to.append(comment.id)

            comment.reply(comment_reply)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print(comments_replied_to)
    print("Sleeping for ten seconds...")
    # Sleep for ten seconds
    time.sleep(10)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(r, comments_replied_to)
