from model import RegisteredUser, Post
from constants import CELEBRITY_FOLLOWERS_COUNT


class RegisteredUserService:
    def __init__(self, registered_user: RegisteredUser):
        self.registered_user = registered_user

    def add_followers(self, follower: RegisteredUser):
        if follower in self.followers:
            print("You are already being followed by this user")
        else:
            self.user.followers.append(follower)
            if len(self.user.followers) >= CELEBRITY_FOLLOWERS_COUNT:
                self.user.is_celebrity = True

    def check_celebrity(self):
        return self.user.is_celebrity

    def view_post(self, post: Post):
        self.user.feed.remove(post)

    def add_post(self, post: Post):
        self.user.timeline.append(post)
        for follower in self.user.followers:
            follower.feed.append(post)

    def follow(self, followee: RegisteredUser):
        if followee in self.user.followings:
            print("You are already following")
        else:
            self.user.followings.append(followee)

