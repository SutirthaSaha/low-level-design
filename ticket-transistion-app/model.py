from abc import ABC, abstractmethod

from enums import TicketState


class User:
    def __init__(self, value: str):
        self.value = value


class State(ABC):
    @abstractmethod
    def start_analysis(self, ticket: 'Ticket') -> bool:
        pass

    @abstractmethod
    def start_review(self, ticket: 'Ticket') -> bool:
        pass

    @abstractmethod
    def mark_done(self, ticket: 'Ticket') -> bool:
        pass


class Ticket:
    def __init__(self, description: str, user: 'User', state: 'State'):
        self.description = description
        self.user = user
        self.state = state

    def get_description(self):
        return self.description

    def get_state(self):
        return self.state

    def set_ticket_state(self, state: 'State'):
        self.state = state


class Analysis(State):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if Analysis._instance is not None:
            raise Exception("Analysis object already created")
        else:
            Analysis._instance = self

    def start_analysis(self, ticket: 'Ticket') -> bool:
        print("Ticket in the same state")
        return False

    def start_review(self, ticket: 'Ticket') -> bool:
        print(f"{ticket.get_description()} moved from {TicketState.ANALYSIS.value} to {TicketState.REVIEW.value}")
        return True

    def mark_done(self, ticket: 'Ticket') -> bool:
        print(f"{ticket.get_description()} moved from {TicketState.ANALYSIS.value} to {TicketState.DONE.value}."
              f"This has to move to Review first.")
        return False


class Review(State):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if Review._instance is not None:
            raise Exception("Review object already created")
        else:
            Review._instance = self

    def start_analysis(self, ticket: 'Ticket'):
        print(f"{ticket.get_description()} moved from {TicketState.REVIEW.value} to {TicketState.ANALYSIS.value}."
              f"Look into it.")
        return True

    def start_review(self, ticket: 'Ticket'):
        print("Ticket in the same state")
        return False

    def mark_done(self, ticket: 'Ticket'):
        print(f"{ticket.get_description()} moved from {TicketState.REVIEW.value} to {TicketState.DONE.value}."
              f"Congratulations!")
        return True


class Done(State):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if Done._instance is not None:
            raise Exception("Done object already created")
        else:
            Done._instance = self

    def start_analysis(self, ticket: 'Ticket'):
        print(
            f"{ticket.get_description()} moved from {TicketState.DONE.value} to {TicketState.ANALYSIS.value}."
            f"Reopened the ticket.")
        return True

    def start_review(self, ticket: 'Ticket') -> bool:
        print(
            f"{ticket.get_description()} moved from {TicketState.DONE.value} to {TicketState.REVIEW.value}. "
            f"Reopened the ticket.")
        return True

    def mark_done(self, ticket: 'Ticket'):
        print("Ticket in the same state")
        return False
