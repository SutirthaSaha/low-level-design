from model import User, Ticket, Review, Analysis, Done
from enums import TicketState
import threading

class TicketService:

    def __init__(self):
        self.lock = threading.Lock()

    def create_ticket(self, desc: str, user: User):
        return Ticket(desc, user, Analysis.get_instance())

    def start_analysis(self, ticket: Ticket):
        with self.lock:
            is_feasible = ticket.get_state().start_analysis(ticket)
            if is_feasible:
                ticket.set_state(Analysis.get_instance())

    def start_review(self, ticket: Ticket):
        with self.lock:
            is_feasible = ticket.get_state().start_review(ticket)
            if is_feasible:
                ticket.set_state(Review.get_instance())

    def mark_done(self, ticket: Ticket):
        with self.lock:
            is_feasible = ticket.get_state().mark_done(ticket)
            if is_feasible:
                ticket.set_state(Done.get_instance())

    def change_ticket_state(self, ticket: Ticket, ticket_state: TicketState):
        if ticket_state == TicketState.ANALYSIS:
            self.start_analysis(ticket)
        elif ticket_state == TicketState.REVIEW:
            self.start_review(ticket)
        else:
            self.mark_done(ticket)
