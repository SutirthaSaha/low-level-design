from datetime import datetime

from model import Admin, Entrance, Exit, ParkingAttendant, ParkingTicket, Vehicle, Cash, Card, ParkingLot, ParkingSpot, \
    ParkingStrategy
from enums import ParkingSpotType
from exceptions import SpotNotFoundException, InvalidVehicleException


class DisplayBoardService:

    def __init__(self):
        self.parking_lot = ParkingLot.get_instance()

    def change(self, parking_spot_type: ParkingSpotType, change: int):
        self.parking_lot.display_board.map[parking_spot_type] += change


class ParkingSpotService:

    def __init__(self):
        self.parking_lot = ParkingLot.get_instance()
        self.display_board_service = DisplayBoardService()

    def create(self, parking_spot_type: ParkingSpotType, floor: int):
        parking_spot = ParkingSpot(parking_spot_type, floor)
        self.parking_lot.free_parking_spots[parking_spot_type].append(parking_spot)
        self.display_board_service.change(parking_spot_type, 1)


class ParkingService:

    def __init__(self, parking_strategy: ParkingStrategy):
        self.parking_lot = ParkingLot.get_instance()
        self.parking_strategy = parking_strategy
        self.parking_attendant_service = ParkingAttendantService()
        self.display_board_service = DisplayBoardService()

    def entry(self, vehicle: Vehicle) -> ParkingTicket:
        parking_spot_type = vehicle.supported_parking_spot_type
        try:
            parking_spot = self.parking_strategy.find_parking_spot(parking_spot_type)
            self.parking_lot.free_parking_spots[parking_spot_type].remove(parking_spot)
            self.parking_lot.occupied_parking_spots[parking_spot_type].append(parking_spot)

            parking_ticket = self.parking_attendant_service.create_parking_ticket(vehicle, parking_spot)

            self.display_board_service.change(parking_spot_type, -1)
            return parking_ticket
        except SpotNotFoundException as snfe:
            raise snfe
        except:
            return None

    def exit(self, parking_ticket: ParkingTicket, vehicle: Vehicle):
        if parking_ticket.vehicle == vehicle:
            parking_spot = parking_ticket.parking_spot
            cost = parking_spot.cost
            self.parking_lot.free_parking_spots[parking_spot.type].append(parking_spot)
            self.parking_lot.occupied_parking_spots[parking_spot.type].remove(parking_spot)

            self.display_board_service.change(parking_spot.type, +1)
            return cost
        else:
            raise InvalidVehicleException('This is an invalid ticket')


class AdminService:
    def __init__(self, admin: Admin):
        self.admin = admin

    def create_entrance(self, name: str):
        entrance = Entrance(name)
        self.admin.parking_lot.entrances.append(entrance)

    def create_exit(self, name: str):
        exit = Exit(name)
        self.admin.parking_lot.exits.append(exit)


class ParkingAttendantService:
    def __init__(self, parking_attendant: ParkingAttendant):
        self.parking_attendant = parking_attendant

    def set_parking_attendant(self, parking_attendant: ParkingAttendant):
        self.parking_attendant = parking_attendant

    def create_parking_ticket(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        parking_ticket = ParkingTicket(vehicle, parking_spot, datetime.now(), self.parking_attendant)
        return parking_ticket


class PaymentService:
    def accept_cash(self, amount):
        cash_payment = Cash()
        cash_payment.initiate_payment(amount)

    def accept_card(self, card_number, cvv, amount):
        card_payment = Card(card_number, amount)
        card_payment.initiate_payment(amount)
