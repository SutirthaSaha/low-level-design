from model import User, Ticket
from enums import TicketState

class TicketService:
    def create_ticket(self, desc: str, user: User):
        return Ticket(desc, user, TicketState.ANALYSIS)

    def change_ticket_state(self, ticket: Ticket, ticket_state: TicketState):
        current_state = ticket.get_ticket_state()
        if current_state == TicketState.ANALYSIS:
            if ticket_state == TicketState.REVIEW:
                print(f"{ticket.get_description()} moved from {current_state.name} to {ticket_state.name}")
            elif ticket_state == TicketState.DONE:
                print(f"{ticket.get_description()} moved from {current_state.name} to {ticket_state.name}. "
                      f"This has to move to Review first.")
                raise Exception("Invalid Transition")
            else:
                print("Ticket in the same state")
        elif current_state == TicketState.REVIEW:
            if ticket_state == TicketState.ANALYSIS:
                print(f"{ticket.get_description()} moved from {current_state.name} to {ticket_state.name}. Look into it.")
            elif ticket_state == TicketState.DONE:
                print(f"{ticket.get_description()} moved from {current_state.name} to {ticket_state.name}. Congratulations!")
            else:
                print("Ticket in the same state")
        else:
            if ticket_state == TicketState.REVIEW:
                print(f"{ticket.get_description()} moved from {current_state.name} to {ticket_state.name}. Reopened the ticket.")
            elif ticket_state == TicketState.DONE:
                print(f"{ticket.get_description()} moved from {current_state.name} to {ticket_state.name}. Reopened the ticket.")
            else:
                print("Ticket in the same state")
        ticket.set_ticket_state(ticket_state)
