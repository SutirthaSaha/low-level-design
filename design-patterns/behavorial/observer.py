from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict
from enum import Enum


class Subscriber(ABC):
    @abstractmethod
    def update(self):
        pass


class EntityType(Enum):
    NEWSPAPER = "NEWSPAPER"
    JOURNAL = "JOURNAL"
    EMAIL = "EMAIL"


class Publisher:
    def __init__(self):
        self.subscribers: Dict[EntityType, Subscriber] = defaultdict(list)

    def subscribe(self, entity_type: EntityType, subscriber: Subscriber):
        self.subscribers[entity_type].append(subscriber)

    def unsubscribe(self, entity_type: EntityType, subscriber: Subscriber):
        self.subscribers[entity_type].remove(subscriber)

    def notify_subscribers(self, entity_type: EntityType):
        for subscriber in self.subscribers[entity_type]:
            subscriber.update()


class NewspaperSubscriber(Subscriber):

    def update(self):
        print("Open door, pickup newspaper and read it")


class JournalSubscriber(Subscriber):

    def update(self):
        print("Buy and read journal")


class EmailSubscriber(Subscriber):
    def update(self):
        print("Open mail and read the newsletter")


if __name__ == '__main__':
    publisher = Publisher()

    news_subscriber_1 = NewspaperSubscriber()
    news_subscriber_2 = NewspaperSubscriber()

    journal_subscriber_1 = JournalSubscriber()

    email_subscriber_1 = EmailSubscriber()
    email_subscriber_2 = EmailSubscriber()
    email_subscriber_3 = EmailSubscriber()

    publisher.subscribe(EntityType.NEWSPAPER, news_subscriber_1)
    publisher.subscribe(EntityType.NEWSPAPER, news_subscriber_2)

    publisher.subscribe(EntityType.JOURNAL, journal_subscriber_1)

    publisher.subscribe(EntityType.EMAIL, email_subscriber_1)
    publisher.subscribe(EntityType.EMAIL, email_subscriber_2)
    publisher.subscribe(EntityType.EMAIL, email_subscriber_3)

    while True:
        choice = int(input("1. Newspaper 2. Journal 3. Email \nWhat do you want to publish? ").strip())
        if choice == 1:
            publisher.notify_subscribers(EntityType.NEWSPAPER)
        elif choice == 2:
            publisher.notify_subscribers(EntityType.JOURNAL)
        elif choice == 3:
            publisher.notify_subscribers(EntityType.EMAIL)
        else:
            break
