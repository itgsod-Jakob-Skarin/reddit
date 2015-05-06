from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_about = "https://oauth.reddit.com/api/v1/user/I_might_be_bot/about"


class User(object):

    def __init__(self, reddit_id):
        self.id = reddit_id

    def me(self):

        pprint(reddit.client.request(url_me))




