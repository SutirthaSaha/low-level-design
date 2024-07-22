from abc import ABC, abstractmethod
from datetime import datetime
from random import randint
from typing import List, Dict
from enums import ParkingSpotType, VehicleType
from exceptions import SpotNotFoundException


class Entrance:
    def __init__(self, name: str):
        self.name = name


class Exit:
    def __init__(self, name: str):
        self.name = name


class ParkingSpot:
    parking_spot_cost_map = {
        ParkingSpotType.MINI: 50,
        ParkingSpotType.COMPACT: 200,
        ParkingSpotType.LARGE: 500,
    }

    def __init__(self, parking_spot_type: ParkingSpotType, floor: int):
        self.id = randint(1, 100)
        self.type = parking_spot_type
        self.cost = ParkingSpot.parking_spot_cost_map[parking_spot_type]
        self.floor = floor
        self.is_free = True


class Vehicle:
    supported_parking_spot_type_map = {
        VehicleType.BIKE: ParkingSpotType.MINI,
        VehicleType.CAR: ParkingSpotType.COMPACT,
        VehicleType.TRUCK: ParkingSpotType.LARGE,
    }

    def __init__(self, vehicle_type: VehicleType):
        self.id = randint(1, 100)
        self.vehicle_type = vehicle_type
        self.supported_parking_spot_type = Vehicle.supported_parking_spot_type_map[vehicle_type]


class DisplayBoard:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if DisplayBoard._instance is not None:
            raise Exception('The instance already exists')
        else:
            DisplayBoard._instance = self


class ParkingLot:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception('The instance already exists')
        else:
            self.id = randint(1, 100)
            self.entrances: List[Entrance] = []
            self.exits: List[Exit] = []
            self.free_parking_spots: Dict[ParkingSpotType, List[ParkingSpot]] = dict()
            self.occupied_parking_spots: Dict[ParkingSpotType, List[ParkingSpot]] = dict()
            self.display_board = DisplayBoard()

            ParkingLot._instance = self


class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Admin(User):
    def __init__(self, username, password, parking_lot: ParkingLot):
        super().__init__(username, password)
        self.parking_lot = parking_lot


class ParkingAttendant(User):
    def __init__(self, username, password):
        super().__init__(username, password)


class ParkingTicket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot, timestamp: datetime,
                 parking_attendant: ParkingAttendant):
        self.id = randint(1, 100)
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.timestamp = timestamp
        self.parking_attendant = parking_attendant


class Payment(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass


class Cash(Payment):
    def initiate_payment(self, amount):
        print(f"Payment of {amount} successful by cash")


class Card(Payment):
    def __init__(self, card_number: str, cvv: int):
        self.card_number = card_number
        self.cvv = cvv

    def initiate_payment(self, amount):
        print(f"Payment of {amount} successful by card")


class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, parking_spot_type: ParkingSpotType):
        pass


class NearestFirstParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_spot_type: ParkingSpotType):
        parking_lot = ParkingLot.get_instance()
        free_parking_spots = parking_lot.free_parking_spots[parking_spot_type]
        if len(free_parking_spots) == 0:
            raise SpotNotFoundException('There are no free spots available')
        return free_parking_spots[0]


class FarthestFirstParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_spot_type: ParkingSpotType):
        parking_lot = ParkingLot.get_instance()
        free_parking_spots = parking_lot.free_parking_spots[parking_spot_type]
        if len(free_parking_spots) == 0:
            raise SpotNotFoundException('There are no free spots available')
        return free_parking_spots[-1]
