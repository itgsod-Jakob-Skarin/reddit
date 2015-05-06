from reddit import client
from reddit.user import User
from reddit.reddits import Subreddit
from reddit.reddits import Comments

jakob = client.login('I_might_be_bot')

lol = Subreddit("leagueoflegends", "")

lol_Comments = Comments("leagueoflegends", "comments")

lol_post_authors = Subreddit("leagueoflegends", "0")

print lol_post_authors.author()

#print lol.new()

#print lol.hot()

#print lol_Comments.comment()

#jakob.me()
#Subreddit.("leagueoflegends")




# python = Subreddit("python")
#
# python.hot()








