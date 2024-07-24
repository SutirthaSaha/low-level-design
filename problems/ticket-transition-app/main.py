from service import TicketService
from model import User
from enums import TicketState

ticket_service = TicketService()

user = User("User 1")
ticket = ticket_service.create_ticket("Demo Ticket", user)
ticket_service.change_ticket_state(ticket, TicketState.DONE)
