import praw
import time
import re
import pprint





reddit = praw.Reddit('bot1')

replied_to = []

while True:
    conversations = reddit.subreddit("bdoghomieg123").modmail.conversations(state='all', sort= 'unread', limit=3)
    for conv in conversations:
        for message in conv.messages:
            messagetext = str(message.body_markdown)
            if messagetext in replied_to:
                print("already replied to:")
                print(message)
                pass
            elif "ban" in messagetext:
                conv.reply("That is up to mod vote at the moment. \n\n\n\n ^(This reply was made by a bot. If bot replied incorrectly, please notify the creator of this bot u/kapow-bitch)")
                print("replied")
                replied_to.append(messagetext)

            conv.read()
            
