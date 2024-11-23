from model import ParkingLot, Admin, Entrance, Exit, Vehicle, ParkingAttendant, ParkingTicket, Cash, Card, ParkingSpot
from abc import ABC, abstractmethod
from enums import ParkingSpotType
from exceptions import InvalidVehicleException, SpotNotFoundException


class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, parking_lot: ParkingLot, parking_spot_type: ParkingSpotType):
        pass


class NearestFirstParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_lot: ParkingLot, parking_spot_type: ParkingSpotType):
        parking_spots = parking_lot.parking_spots[parking_spot_type]
        for parking_spot in parking_spots:
            if parking_spot.available:
                parking_spot.available = False
                return parking_spot
        return None


class FarthestFirstParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_lot: ParkingLot, parking_spot_type: ParkingSpotType):
        parking_spots = parking_lot.parking_spots[parking_spot_type]
        for parking_spot in parking_spots[::-1]:
            if parking_spot.available:
                parking_spot.available = False
                return parking_spot
        return None


class AdminService:
    def __init__(self, admin: Admin):
        self.admin = admin

    def add_entrance(self, name: str):
        self.admin.parking_lot.add_entrance(Entrance(name))

    def add_exit(self, name: str):
        self.admin.parking_lot.add_exit(Exit(name))

    def remove_entrance(self, entrance: Entrance):
        self.admin.parking_lot.remove_entrance(entrance)

    def remove_exit(self, exit: Exit):
        self.admin.parking_lot.remove_exit(exit)


class ParkingAttendantService:
    def __init__(self):
        self.parking_attendant = None

    def set_parking_attendant(self, parking_attendant: ParkingAttendant):
        self.parking_attendant = parking_attendant

    def create_parking_ticket(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        return ParkingTicket(vehicle, parking_spot, self.parking_attendant)


class PaymentService:
    def accept_cash(self, amount: int):
        cash = Cash()
        cash.initiate_payment(amount)

    def accept_card(self, card_number: str, cvv: int, amount: int):
        card = Card(card_number, cvv)
        card.initiate_payment(amount)


class ParkingService:
    def __init__(self, parking_lot: ParkingLot, parking_strategy: ParkingStrategy,
                 parking_attendant_service: ParkingAttendantService, payment_service: PaymentService):
        self.parking_lot = parking_lot
        self.parking_strategy = parking_strategy
        self.parking_attendant_service = parking_attendant_service
        self.payment_service = payment_service

    def entry(self, vehicle: Vehicle):
        parking_spot = self.parking_strategy.find_parking_spot(self.parking_lot, vehicle.parking_spot_type)
        if parking_spot:
            parking_ticket = self.parking_attendant_service.create_parking_ticket(vehicle, parking_spot)
            self.parking_lot.display_board.update(vehicle.parking_spot_type, -1)
            return parking_ticket
        else:
            raise SpotNotFoundException("No valid parking spot for your vehicle found")

    def exit(self, parking_ticket: ParkingTicket, vehicle: Vehicle):
        if parking_ticket.vehicle != vehicle:
            raise InvalidVehicleException("Invalid vehicle for the parking ticket")
        parking_ticket.parking_spot.available = True
        self.parking_lot.display_board.update(vehicle.parking_spot_type, 1)
        amount = parking_ticket.parking_spot.cost
        return amount
