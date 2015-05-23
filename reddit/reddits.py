from pprint import pprint

import reddit


url_me = "https://oauth.reddit.com/api/v1/me"
url_hot = "https://oauth.reddit.com/r/{subreddit}/hot"
url = "https://oauth.reddit.com/r/{subreddit}/comments"
url_new = "https://oauth.reddit.com/r/{subreddit}/new"


class Subreddit(object):

    def __init__(self, subreddit, author):
        self.subreddit = subreddit
        #self._author = author
        self._posts = []


    def hot(self):
        res = reddit.client.request(url_hot.format(subreddit=self.subreddit))

        hot_posts = []

        for p in res['data']['children']:
            hot_posts.append(p['data'])

        return hot_posts

    def new(self):
        pprint(reddit.client.request(url_new.format(subreddit=self.subreddit)))

    def posts(self):

        res = reddit.client.request(url_hot.format(subreddit=self.subreddit, author=self.author))

        _posts = []
        i = 0

        for p in res['data']['children']:
            i += 1
            p['nr'] = i
            _posts.append(Post(p))

        return _posts

    def author(self):

        class Post(object):

            def __init__(self, post):
                self.post = post


class Post(object):
    pass

    def __init__(self ,data):
        self.nr = data['nr']
        self.link = data['data']['url']

        self.title = data['data']['title']
        self.author = data['data']['author']

    def __str__(self):
        return "Post nr: " + str(self.nr) + "\nTitle: " + self.title + "\nAuthor: " + self.author + "\nlink: " + self.link + "\n"


class Comments(object):

    def __init__(self, subreddit, comments):
        self.subreddit = subreddit
        self.comments = comments

    def comment(self):
        pprint(reddit.client.request(url.format(subreddit=self.subreddit, comments=self.comments)))