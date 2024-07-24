from enum import Enum


class ParkingSpotType(Enum):
    MINI = 'MINI'
    COMPACT = 'COMPACT'
    LARGE = 'LARGE'


class VehicleType(Enum):
    BIKE = 'BIKE'
    CAR = 'CAR'
    TRUCK = 'TRUCK'
