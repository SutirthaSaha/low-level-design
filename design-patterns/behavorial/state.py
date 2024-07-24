from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def to_to_do(self):
        pass

    @abstractmethod
    def to_in_progress(self):
        pass

    @abstractmethod
    def to_done(self):
        pass


class ToDo(State):

    def to_to_do(self):
        print("Ticket is already in to-do state")

    def to_in_progress(self):
        print("Ticket moved to in-progress")

    def to_done(self):
        raise Exception("Ticket can't be moved directly to done from to-do")


class InProgress(State):

    def to_to_do(self):
        print("Ticket moved back to to-do")

    def to_in_progress(self):
        print("Ticket already in in-progress state")

    def to_done(self):
        print("Ticket moved to done state")


class Done(State):

    def to_to_do(self):
        print("Moving ticket from done to analysis. DANGER move.")

    def to_in_progress(self):
        print("Moving ticket from done to in-progress. DANGER move.")

    def to_done(self):
        print("Ticket already in done state")


class Ticket:
    def __init__(self, description: str):
        self.description = description
        self.state = ToDo()

    def to_to_do(self):
        self.state.to_to_do()
        self.state = ToDo()

    def to_in_progress(self):
        self.state.to_in_progress()
        self.state = InProgress()

    def to_done(self):
        self.state.to_done()
        self.state = Done()


if __name__ == '__main__':
    ticket = Ticket("Generic Ticket")
    ticket.to_in_progress()
    ticket.to_done()
