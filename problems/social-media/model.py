from random import randint
from abc import ABC
from typing import List


class Comment:
    def __init__(self, post: 'Post', user: 'RegisteredUser'):
        self.post = post
        self.user = user


class Post:
    def __init__(self, image_url: str, caption: str, user: 'RegisteredUser'):
        self.image_url = image_url
        self.caption = caption
        self.user = user
        self.comments = []


class Timeline:
    def __init__(self):
        self.posts = []


class Feed:
    def __init__(self):
        self.posts = []


class User(ABC):
    def __init__(self, username: str, password: str):
        self.id = randint(1, 100)
        self.username = username
        self.password = password
        self.name = None
        self.phone = None

    def set_name(self, name: str):
        self.name = name

    def set_phone(self, phone: str):
        self.phone = phone


class RegisteredUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.feed = Feed()
        self.timeline = Timeline()
        self.followers: List[User] = []
        self.followings: List[User] = []
        self.is_celebrity = False
