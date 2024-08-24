from model import UserRateLimiter
from enums import Policy
import time


if __name__ == "__main__":
    policy = Policy.SLIDING_WINDOW
    user_ratelimiter = UserRateLimiter(policy)

    user_id = 1
    user_ratelimiter.add_user(user_id)

    for i in range(10):
        user_ratelimiter.access_application(user_id)
        time.sleep(1)