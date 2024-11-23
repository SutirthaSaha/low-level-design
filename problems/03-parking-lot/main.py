from model import *
from service import *

def main():
    # Setting up the parking lot and services
    parking_lot = ParkingLot("Main Parking Lot")
    admin = Admin("Admin1", "admin1@example.com", "password", parking_lot)
    parking_attendant = ParkingAttendant("Attendant1", "attendant1@example.com", "password")

    admin_service = AdminService(admin)
    parking_attendant_service = ParkingAttendantService()
    parking_attendant_service.set_parking_attendant(parking_attendant)
    payment_service = PaymentService()

    parking_strategy = NearestFirstParkingStrategy()
    parking_service = ParkingService(parking_lot, parking_strategy, parking_attendant_service, payment_service)

    # Adding entrances, exits, and parking spots
    admin_service.add_entrance("Entrance1")
    admin_service.add_exit("Exit1")

    compact_spot = CompactParkingSpot(floor_num=1)
    mini_spot = MiniParkingSpot(floor_num=1)
    large_spot = LargeParkingSpot(floor_num=1)

    parking_lot.add_parking_spot(compact_spot, ParkingSpotType.COMPACT)
    parking_lot.add_parking_spot(mini_spot, ParkingSpotType.MINI)
    parking_lot.add_parking_spot(large_spot, ParkingSpotType.LARGE)

    # Vehicle Entry
    vehicle = Car("CAR123")
    parking_ticket = parking_service.entry(vehicle)
    print(f"Parking Ticket ID: {parking_ticket.id}")

    # Vehicle Exit
    amount_due = parking_service.exit(parking_ticket, vehicle)
    print(f"Amount Due: {amount_due}")

    # Payment
    card = Card("1234567890123456", 123)
    payment_service.accept_card(card.card_number, card.cvv, amount_due)


if __name__ == "__main__":
    main()