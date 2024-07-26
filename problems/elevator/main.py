from enum import Enum
from abc import ABC, abstractmethod
from typing import List


class ElevatorState(Enum):
    STOPPED: "Stopped"
    MOVING_UP: "Moving Up"
    MOVING_DOWN: "Moving Down"


class FloorButtonType(Enum):
    UP: "UP"
    DOWN: "DOWN"


class ElevatorInput(ABC):
    def __init__(self):
        pass

class Card(ElevatorInput):
    def __init__(self):
        pass


class Button(ElevatorInput):
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False


class FloorButton(Button):
    def __init__(self, floor_button_type: FloorButtonType):
        self.floor_button_type = floor_button_type


class Floor:
    def __init__(self, number):
        self.number = number
        self.up_button = FloorButton(FloorButtonType.UP)
        self.down_button = FloorButton(FloorButtonType.DOWN)


class ElevatorButton(Button):
    def __init__(self, floor: Floor):
        self.floor = floor


class Elevator(ABC):
    def __init__(self, floor_count: int):
        self.floors: List[Floor] = []
        for floor_number in floor_count:
            floor = Floor(floor_number)
            self.floors.append(floor)
        self.state = ElevatorState.STOPPED
        self.current_floor = self.floors[0]
        self.next_floors: List[Floor] = []

    @abstractmethod
    def accept(self, elevator_input: ElevatorInput):
        pass

class ActionButtonStrategy(ABC):

    @abstractmethod
    def accept(self, elevator: 'ButtonElevator', button: Button):
        pass


class ActionElevatorButtonStrategy(ActionButtonStrategy):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if ActionElevatorButtonStrategy._instance is not None:
            raise Exception("Instance already defined")
        ActionElevatorButtonStrategy._instance = self

    def accept(self, elevator: 'ButtonElevator', button: Button):
        pass


class ActionFloorButtonStrategy(ActionButtonStrategy):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if ActionFloorButtonStrategy._instance is not None:
            raise Exception("Instance already defined")
        ActionFloorButtonStrategy._instance = self

    def accept(self, elevator: 'ButtonElevator', button: Button):
        pass


class ButtonElevator(Elevator):
    def __init__(self, floor_count: int):
        super().__init__(floor_count)
        self.buttons: List[ElevatorButton] = []
        for floor in self.floors:
            button = ElevatorButton(floor)
            self.buttons.append(button)

    def accept(self, elevator_input: Button):
        if type(elevator_input) is FloorButton:
            ActionFloorButtonStrategy.get_instance().accept(self, elevator_input)
        else:
            ActionElevatorButtonStrategy.get_instance().accept(self, elevator_input)
