import string
import random
from typing import List, Dict
from abc import ABC, abstractmethod
from collections import defaultdict

from datetime import datetime
from enums import ParkingSpotType


def generate_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))  # Choose three random uppercase letters
    return letters


class Entrance:
    def __init__(self, name: str):
        self.name = name


class Exit:
    def __init__(self, name: str):
        self.name = name


class DisplayBoard:
    def __init__(self):
        self.counter = defaultdict(int)

    def update(self, parking_spot_type: ParkingSpotType, change: int):
        self.counter[parking_spot_type.value] += change


class ParkingSpot(ABC):
    def __init__(self, floor_num: int, cost: int):
        self.id: str = generate_id()
        self.floor_num: int = floor_num
        self.cost: int = cost
        self.available: bool = True


class CompactParkingSpot(ParkingSpot):
    def __init__(self, floor_num: int):
        super().__init__(floor_num, 20)


class MiniParkingSpot(ParkingSpot):
    def __init__(self, floor_num: int):
        super().__init__(floor_num, 50)


class LargeParkingSpot(ParkingSpot):
    def __init__(self, floor_num: int):
        super().__init__(floor_num, 100)


class ParkingLot:
    def __init__(self, name: str):
        self.name: str = name
        self.entrances: List[Entrance] = []
        self.exits: List[Exit] = []
        self.display_board = DisplayBoard()
        self.parking_spots: Dict[ParkingSpotType, List[ParkingSpot]] = defaultdict(list)

    def add_entrance(self, entrance: Entrance):
        self.entrances.append(entrance)

    def add_exit(self, exit: Exit):
        self.exits.append(exit)

    def remove_entrance(self, entrance: Entrance):
        self.entrances.remove(entrance)

    def remove_exit(self, exit: Exit):
        self.exits.remove(exit)

    def add_parking_spot(self, parking_spot: ParkingSpot, parking_spot_type: ParkingSpotType):
        self.parking_spots[parking_spot_type].append(parking_spot)
        self.display_board.update(parking_spot_type, 1)


class Vehicle(ABC):
    def __init__(self, id: str, parking_spot_type: ParkingSpotType):
        self.id = id
        self.parking_spot_type = parking_spot_type


class MotorBike(Vehicle):
    def __init__(self, id: str):
        super().__init__(id, ParkingSpotType.COMPACT)


class Car(Vehicle):
    def __init__(self, id: str):
        super().__init__(id, ParkingSpotType.MINI)


class Truck(Vehicle):
    def __init__(self, id: str):
        super().__init__(id, ParkingSpotType.LARGE)


class Account(ABC):
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class Admin(Account):
    def __init__(self, name: str, email: str, password: str, parking_lot: ParkingLot):
        super().__init__(name, email, password)
        self.parking_lot = parking_lot


class ParkingAttendant(Account):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)


class ParkingTicket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot,
                 parking_attendant: ParkingAttendant):
        self.id: str = generate_id()
        self.vehicle: Vehicle = vehicle
        self.parking_spot = parking_spot
        self.timestamp = datetime.now()
        self.parking_attendant = parking_attendant


class PaymentMethod(ABC):
    @abstractmethod
    def initiate_payment(self, amount: int):
        pass


class Cash(PaymentMethod):
    def initiate_payment(self, amount: int):
        print(f"{amount} received in cash")


class Card(PaymentMethod):
    def __init__(self, card_number: str, cvv: int):
        self.card_number: str = card_number
        self.cvv: int = cvv

    def initiate_payment(self, amount: int):
        print(f"{amount} received by card")
