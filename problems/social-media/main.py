from datetime import datetime
from enum import Enum
from abc import ABC
from random import randint
from typing import List, Dict
from collections import defaultdict
from constants import CELEBRITY_FOLLOWERS_COUNT


class PostType(Enum):
    TWEET = "Tweet"
    COMMENT = "Comment"


class LikeType(Enum):
    LIKE = "=|"
    SAD = ":("
    HEART = "<3"


class User(ABC):
    def __init__(self, name: str, email: str, password: str, contact_number: str):
        self.id = randint(1, 100)
        self.name = name
        self.email = email
        self.password = password
        self.contact_number = contact_number


class Like:
    def __init__(self, user: 'RegisteredUser', post_type: PostType, like_type: LikeType):
        self.user = user
        self.post_type = post_type
        self.like_type = like_type


class Comment:
    def __init__(self, user: 'RegisteredUser', content: str):
        self.user = user
        self.content = content
        self.likes: List[Like] = []

    def get_content(self):
        return self.content

    def add_like(self, user: 'RegisteredAccount', like_type: LikeType):
        like = Like(user, PostType.COMMENT, like_type)
        self.likes.append(like)

    def remove_like(self, user: 'RegisteredAccount'):
        remove_like = None
        for like in self.likes:
            if like.user == user:
                remove_like = like
                break
        if remove_like:
            self.likes.remove(remove_like)


class CommentThread:
    def __init__(self):
        self.id = randint(1, 10)
        self.comments: List[Comment] = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments


class Tweet:
    def __init__(self, user: 'RegisteredUser', content: str, hashtags: List[str], tagged_users: List['RegisteredUser']):
        self.id = randint(1, 10)
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.comment_threads: Dict[int, CommentThread] = dict()
        self.hashtags: List[str] = hashtags
        self.tagged_users = tagged_users
        self.likes: List[Like] = []

    def add_comment(self, user: 'RegisteredUser', content: str, thread=None):
        comment = Comment(user, content)
        if thread is None:
            thread = CommentThread()
            self.comment_threads[thread.id] = thread
        thread.add_comment(comment)

    def add_like(self, user: 'RegisteredUser', like_type: LikeType):
        like = Like(user, PostType.TWEET, like_type)
        self.likes.append(like)

    def remove_like(self, user: 'RegisteredUser'):
        remove_like = None
        for like in self.likes:
            if like.user == user:
                remove_like = like
                break
        self.likes.remove(remove_like)


class TimelineWall(ABC):
    def __init__(self):
        self.tweets: List[Tweet] = []

    def get_tweets(self):
        return self.tweets

    def add_tweet(self, tweet: Tweet):
        self.tweets.append(tweet)


class Timeline(TimelineWall):
    def __init__(self):
        super().__init__()

    def add_celebrity_tweets(self, tweets: List[Tweet]):
        self.tweets.extend(tweets)


class Wall(TimelineWall):
    def __init__(self):
        super().__init__()


class ContentServer:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if ContentServer._instance is not None:
            raise Exception("Content Server instance already exists")
        else:
            self.subscribers: Dict['RegisteredUser', List['RegisteredUser']] = defaultdict(list)
            self.celeb_tweets: Dict['RegisteredUser', List['RegisteredUser']] = defaultdict(list)
            ContentServer._instance = self

    def add_subscriber(self, follower: 'RegisteredUser', followee: 'RegisteredUser'):
        self.subsribers[followee].append(follower)

    def notify(self, tweet: Tweet):
        user = tweet.user
        if user.check_celebrity:
            self.celeb_tweets[user].append(tweet)
        else:
            for follower in user.followers:
                follower.get_timeline().tweets.append(tweet)

    def get_celeb_tweets(self, user: 'RegisteredUser'):
        return self.celeb_tweets[user]


class RegisteredUser(User):
    def __init__(self):
        self.wall = Wall()
        self.timeline = Timeline()
        self.followers: List[RegisteredUser] = []
        self.following: List[RegisteredUser] = []

    def check_celebrity(self):
        if len(self.followers) > CELEBRITY_FOLLOWERS_COUNT:
            return True
        return False

    def get_timeline(self) -> Timeline:
        return self.timeline

    def show_timeline(self):
        normal_tweets = self.get_timeline().get_tweets()
        celeb_tweets = []
        for following in self.following:
            if following.check_celebrity():
                celeb_tweets.extend(ContentServer.get_instance().get_celeb_tweets[following])
        tweets = normal_tweets + celeb_tweets
        return tweets

    def post_tweet(self, tweet: Tweet):
        self.wall.add_tweet(tweet)
        ContentServer.get_instance().notify(tweet)

    def add_follower(self, user: 'RegisteredUser'):
        self.followers.append(user)
        ContentServer.get_instance().add_subsriber(follower=user, followee=self)

    def add_followee(self, user: 'RegisteredUser'):
        self.following.add(user)
        ContentServer.get_instance().add_subscriber(follower=self, followee=user)

    def add_like_tweet(self, tweet: Tweet, like_type: LikeType):
        tweet.add_like(self, like_type)

    def remove_like_tweet(self, tweet: Tweet):
        tweet.remove_like(self)

    def add_comment(self, tweet: Tweet, content: str):
        tweet.add_comment(self, content)

    def add_like_comment(self, comment: Comment, like_type: LikeType):
        comment.add_like(self, like_type)

    def remove_like_comment(self, comment: Comment):
        comment.remove_like(self)
