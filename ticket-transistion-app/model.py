from abc import ABC, abstractmethod

from enums import TicketState


class User:
    def __init__(self, name: str):
        self.name = name


class Ticket:
    def __init__(self, description: str, user: User, ticket_state: TicketState):
        self.description = description
        self.user = user
        self.ticket_state = ticket_state

    def get_description(self):
        return self.description

    def get_ticket_state(self):
        return self.ticket_state

    def set_ticket_state(self, ticket_state: TicketState):
        self.ticket_state = ticket_state
