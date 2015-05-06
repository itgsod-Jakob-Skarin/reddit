from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_hot = "https://oauth.reddit.com/r/{subreddit}/hot"
url = "https://oauth.reddit.com/r/{subreddit}/comments"
url_new = "https://oauth.reddit.com/r/{subreddit}/new"


class Subreddit(object):

    def __init__(self, subreddit, author):
        self.subreddit = subreddit
        self.author = author

    def hot(self):
        #pprint(reddit.client.request(url_hot.format(subreddit=self.subreddit)))
        return reddit.client.request(url_hot.format(subreddit=self.subreddit))

    def new(self):
        pprint(reddit.client.request(url_new.format(subreddit=self.subreddit)))

    class Post(object):

        def __init__(self, post):
            self.post = post

        def author(self):
            return reddit.client.request(url_hot.format(subreddit=self.subreddit, auther=u'user'))


class Comments(object):

    def __init__(self, subreddit, comments):
        self.subreddit = subreddit
        self.comments = comments

    def comment(self):
        pprint(reddit.client.request(url.format(subreddit=self.subreddit, comments=self.comments)))
