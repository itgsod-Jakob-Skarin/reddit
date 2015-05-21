from reddit import client
from reddit.user import User
from reddit.reddits import Subreddit
from reddit.reddits import Comments

jakob = client.login('I_might_be_bot')

lol = Subreddit("leagueoflegends", "")

lol_Comments = Comments("leagueoflegends", "comments")

lol_post_authors = Subreddit("leagueoflegends", "author")

#print lol.posts(2)

for p in lol.posts():
    print p
    #print "Post nr " + str(p.nr) + "\nTitle: \n" + p.title + "\nAuthor: \n" + p.author
    #print p.author






