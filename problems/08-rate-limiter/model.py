from abc import ABC, abstractmethod
from collections import deque
import datetime
from enums import Policy


class RateLimiter(ABC):
    @abstractmethod
    def grant_access(self):
        pass


class SlidingWindowRateLimiter(RateLimiter):
    def __init__(self, bucket_capacity, time_period):
        self.sliding_window = deque()
        self.bucket_capacity = bucket_capacity
        self.time_period = time_period

    def grant_access(self) -> bool:
        current_time = datetime.datetime.now()
        self.update_queue(current_time)
        if len(self.sliding_window) < self.bucket_capacity:
            self.sliding_window.append(current_time)
            return True
        return False

    def update_queue(self, current_time):
        while self.sliding_window:
            difference = current_time - self.sliding_window[0]
            seconds_difference = difference.total_seconds()
            if seconds_difference < self.time_period:
                break
            self.sliding_window.popleft()


class RateLimiterFactory:
    @staticmethod
    def get_rate_limiter(policy: Policy) -> RateLimiter:
        if policy == Policy.SLIDING_WINDOW:
            return SlidingWindowRateLimiter(5, 600)
        raise Exception("Invalid policy.")


class UserRateLimiter:
    def __init__(self, policy: Policy):
        self.bucket = dict()
        self.policy = policy

    def add_user(self, user_id):
        self.bucket[user_id] = RateLimiterFactory.get_rate_limiter(self.policy)

    def access_application(self, user_id):
        if self.bucket[user_id].grant_access():
            print("Able to access")
        else:
            print("429 - Too many requests")
